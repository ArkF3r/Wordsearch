import random
class Palabras:
    def __init__(self, Tipo, numPalabras):
        self.i = 0
        self.Tipo = Tipo
        self.choosenWords = self.selectWords(numPalabras)
        self.Anagramas = self.doAnagrams()
    
    def selectWords(self, numPalabras):
        if(self.Tipo == 0):
            self.Concept = 'GATOS'
            return ['HOLA', 'SALUD', 'CAROLINA', 'CARRO']
        elif(self.Tipo == 1):
            self.Concept = 'TOROS'
            return ['HOLA', 'SALUD', 'CAROLINA', 'CARRO']
        elif(self.Tipo == 2):
            self.Concept = 'COMPUTO'
            return ['HOLA', 'SALUD', 'CAROLINA', 'CARRO']
        elif(self.Tipo == 3):
            self.Concept = 'FRUTA'
            return ['HOLA', 'SALUD', 'CAROLINA', 'CARRO']
        elif(self.Tipo == 4):
            self.Concept = 'FRUTA'
            return ['HOLA', 'SALUD', 'CAROLINA', 'CARRO']
    
    def doAnagrams(self):
        Anagrams = []
        for p in self.choosenWords:
            anagram = random.sample(p, len(p))
            anagram = ''.join(anagram)
            Anagrams.append(anagram)
        return Anagrams

    def getPalabras(self):
        return self.choosenWords

    def getAnagramas(self):
        return self.Anagramas
    
    def hasWord(self, word):
        return word in self.choosenWords
    
    def getNextWord(self):
        S = 0
        if(self.i < len(self.choosenWords)):
            S = self.choosenWords[self.i]
            self.i = self.i + 1
        return S

    