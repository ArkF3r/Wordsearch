from Wordsearch import *
import struct
import socket
import json
import sys
class serverWord:
    def __init__(self, HOST, PORT):
        self.serverAddress = (HOST, PORT)
        self.Juego = Juego()
        self.mensaje = ''
        self.tamMensaje = 0
        self.mensajeParcial = bytearray()

    def initTCP(self):
        try:
            self.serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.serverSock.bind(self.serverAddress)
            print('Iniciando servidor en: %s puerto: %s' % self.serverAddress)
        except Exception as e:
            self.serverSock.close()
            print('Error al iniciar socket')
            print(e)
    
    def Escucha(self):
        self.serverSock.listen(1)
        while True:
            print('Esperando jugador')
            self.client, self.client_address = self.serverSock.accept()
            try:
                print('{}'.format(self.client_address))
                while True:
                    data = self.client.recv(4096)#65536)
                    if data:
                        self.recibirMensaje(data, self.manejadorMensaje)
                    elif not data:
                        print('Cliente desconectado', self.client_address)
                        self.client.close()
                        break
            except Exception as e:
                self.client.close()
                print('Error de conexión con el cliente')
                print(e)      
    
    def recibirMensaje(self, data, callback):
        self.mensajeParcial = self.mensajeParcial+data
        if self.tamMensaje == 0 and len(self.mensajeParcial) >=4:
            self.tamMensaje = int.from_bytes(self.mensajeParcial[0:4], byteorder='little')
        
        if self.tamMensaje != 0 and len( self.mensajeParcial ) >= self.tamMensaje:
            buffer = self.mensajeParcial[4:len(self.mensajeParcial)]
            self.tamMensaje = 0
            self.mensajeParcial = bytearray()
            callback(buffer)

    def manejadorMensaje(self, buffer):
        self.mensaje = buffer
        Obj = str(buffer, 'utf-8')
        Obj = json.loads(Obj)
        Tipo = Obj['Tipo']
        Respuesta = '' 
        if( Tipo == 'Nuevojuego' ):
            Respuesta = self.Juego.nuevoJuego(Obj['Modalidad'], Obj['Dificultad'], Obj['Nick'])
        elif( Tipo == 'Verificapalabra' ):
            Respuesta = self.Juego.verificaPalabra(Obj['Palabra'])
        self.enviarMensaje(Respuesta) 

    def enviarMensaje(self, mensaje): #recibe un string
        bufferT = len(mensaje).to_bytes(4, byteorder='little')
        bufferT = bufferT + bytearray(mensaje, 'utf-8')
        self.client.sendall(bufferT)
        print('Mensaje enviado')

def main():
    s = serverWord('localhost', 10000)
    s.initTCP()
    s.Escucha()
main()
