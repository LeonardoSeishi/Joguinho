from abc import ABC, abstractmethod
import pygame



class Objeto():

    def __init__(self, velocidade, x, y, imagem, largura, altura, aceleracao):
        self.__cordenadas = [x, y]
        self.__altura = altura
        self.__largura = largura
        self.__imagem = pygame.image.load(imagem).convert_alpha()
        self.__velocidade = velocidade
        self.__aceleracao = aceleracao
        self.__objRect = self.imagem.get_rect()
        self.objRect.x = x
        self.objRect.y = y

    @property
    def cordenadas(self):
        return self.__cordenadas

    @property
    def imagem(self):
        return self.__imagem

    @property
    def velocidade(self):
        return self.__velocidade

    @property
    def largura(self):
        return self.__largura

    @property
    def altura(self):
        return self.__altura

    @property
    def aceleracao(self):
        return self.__aceleracao

    @property
    def objRect(self):
        return self.__objRect

    @cordenadas.setter
    def cordenadas(self, cordenadas:list):
        self.__cordenadas = cordenadas

    @imagem.setter
    def imagem(self, imagem):
        self.__imagem = pygame.image.load(imagem).convert_alpha()

    @velocidade.setter
    def velocidade(self, velocidade):
        self.__velocidade = velocidade

    @aceleracao.setter
    def aceleracao(self, A):
        self.__aceleracao = A

    @objRect.setter
    def objRect(self, obj):
        self.__objRect = obj

    def desenha(self, screen):
        screen.blit(self.imagem, self.objRect)

    def atualizar(self):
        self.__velocidade += self.__aceleracao
        self.__cordenadas[0] += self.__velocidade
        self.__objRect = pygame.Rect(self.__cordenadas[0], self.__cordenadas[1], self.__largura, self.__altura)
        if self.__cordenadas[0] < -100:
            self.__cordenadas[0] = 1250
