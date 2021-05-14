from objeto import Objeto
import random 
import pygame

class Obstaculo(Objeto):
    def __init__(self, velocidade, x, y, imagem, largura, altura, aceleracao):
        super().__init__(velocidade, x, y, imagem, largura, altura, aceleracao)
        self.__animacao = 0
        self.__tempo = 0
        self.__img_cacto = random.randint(0,2)

    def desenha(self, screen):
        if len(self.imagem) == 3:
            screen.blit(self.imagem[self.__img_cacto], self.objRect)
        else:
            self.__tempo += 1
            if self.__tempo == 5:
                self.__tempo = 0
                self.__animacao = (self.__animacao + 1) % len(self.imagem)
            screen.blit(self.imagem[self.__animacao], self.objRect)

