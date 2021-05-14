import pygame

class Background():
    def __init__(self, imagem):
        self.__imagem = imagem
        self.__rect = self.__imagem.get_rect()
        self.__imagem1 = imagem
        self.__rect1 = self.__imagem.get_rect()
        self.__rect.bottom = 500
        self.__rect1.bottom = 500
        self.__rect1.left = self.__rect.right
        self.__velocidade = 0
        self.__aceleracao = 0

    @property
    def velocidade(self):
        return self.__velocidade

    @property
    def aceleracao(self):
        return self.__aceleracao

    @velocidade.setter
    def velocidade(self, v):
        self.__velocidade = v

    @aceleracao.setter
    def aceleracao(self, a):
        self.__aceleracao = a

    def desenha(self, screen):
        screen.blit(self.__imagem,self.__rect)
        screen.blit(self.__imagem1,self.__rect1)

    def atualizar(self):
        self.__velocidade += self.__aceleracao
        self.__rect.left += self.__velocidade
        self.__rect1.left += self.__velocidade

        if self.__rect.right < 0:
            self.__rect.left = self.__rect1.right

        if self.__rect1.right < 0:
            self.__rect1.left = self.__rect.right