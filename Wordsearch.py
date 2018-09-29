from time import time
from Palabras import Palabras
import random
import json
class Juego:
    def __init__(self):
        self.numPalabras = 14
        self. Palabras = None
        self.Modalidad = None
        self.Dificultad = None
        self.Tablero = {}

    def nuevoJuego(self, Modalidad, Dificultad, Nick ):
        self.Modalidad = Modalidad
        self.Dificultad = Dificultad
        self.Nick = Nick
        tipoConcepto = random.randint(0,5)
        self.Palabras = Palabras(tipoConcepto, self.numPalabras)
        self.palabrasRestantes = self.numPalabras
        self.timer = time()
        return self.creaMensaje('Datosjuego')

    def verificaPalabra(self, Palabra):
        self.stateLastWord = self.Palabras.hasWord(Palabra)
        if( self.stateLastWord):
            self.palabrasRestantes = self.palabrasRestantes - 1
            if ( self.palabrasRestantes == 0 ):
                self.lastTime = time() - self.timer #Obtener tiempo
                self.verificaScore()
                return self.creaMensaje('Finjuego')
        return self.creaMensaje('RespuestaVerificacion')

    def creaMensaje(self, Tipomensaje):
        Mensaje = {}
        if(Tipomensaje == 'Datosjuego'):
            Mensaje = { 
                'Tipo': Tipomensaje,
                'Palabras': self.Palabras.getPalabras()
            }
            if(self.Modalidad == 'Anagrama' ):
                Mensaje['Anagramas'] = self.Palabras.getAnagramas()
        elif( Tipomensaje == 'RespuestaVerificacion' ):
            Mensaje = {
                'Tipo': Tipomensaje,
                'Estado': self.stateLastWord
            }
            if( self.Dificultad == 'Intermedia' ):
                Mensaje['PalabraPista'] = self.Palabras.getNextWord()
        elif( Tipomensaje == 'Finjuego' ):
            Mensaje = {
                'Tipo': Tipomensaje,
                'Time': self.lastTime,
                'Modalidad': self.Modalidad,
                'Dificultad': self.Dificultad
            }
        Mensaje = json.dumps(Mensaje)
        return Mensaje
        
    def verificaScore(self):
        TabAux = {}
        if(len(self.Tablero) == 0):
            self.Tablero[self.Nick] = {'Tiempo':self.lastTime, 'Dificultad': self.Dificultad, 'Modalidad':self.Modalidad}
        else:
            i = 0
            for a in self.Tablero:
                while(i < len(self.Tablero) or i < 10):
                    if( self.lastTime > self.Tablero[a]['Tiempo'] ):
                        TabAux[self.Nick] = {'Tiempo':self.lastTime, 'Dificultad': self.Dificultad, 'Modalidad':self.Modalidad}
                    else:
                        TabAux[a] = self.Tablero[a]
                    i = i + 1
            self.Tablero = TabAux