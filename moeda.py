from objeto import Objeto
import random 
import pygame


class Moeda(Objeto):
    def __init__(self, velocidade, x, y, imagem, largura, altura, aceleracao):
        super().__init__(velocidade, x, y, imagem, largura, altura, aceleracao)
        self.__animacao = 0
        self.__tempo = 0

    @property
    def colisao(self):
        return self.__colisao

    @colisao.setter
    def colisao(self, boolean):
        self.__colisao = boolean

    def desenha(self, screen):
        self.__tempo += 1
        if self.__tempo == 5:
            self.__tempo = 0
            self.__animacao = (self.__animacao + 1) % len(self.imagem)
        screen.blit(self.imagem[self.__animacao], (self.cordenadas))

    def atualizar(self):
        self.velocidade += self.aceleracao
        self.cordenadas[0] += self.velocidade
        self.objRect = pygame.Rect(self.cordenadas[0], self.cordenadas[1], self.largura, self.altura)

