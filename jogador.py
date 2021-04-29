import pygame
from objeto import Objeto

class Jogador(Objeto):
    def __init__(self, velocidade, x, y, imagem, largura, altura, img_vida):
        super().__init__(velocidade, x, y, imagem, largura, altura)
        self.__vidas = 3
        self.__vidaum = img_vida
        self.__img_vida2 = img_vida
        self.__img_vida3 = img_vida
        self.__gravidade = 0.4
        self.__pulando = False
        self.__agachado = False
        self.__colisao = False


    @property
    def vidas(self):
        return self.__vidas

    @property
    def pulando(self):
        return self.__pulando

    @property
    def agachado(self):
        return self.__agachado

    @property
    def colisao(self):
        return self.__colisao

    @vidas.setter
    def vidas(self, vidas):
        self.__vidas = vidas

    @vidaum.setter
    def vidaum(self, img):
        self.__vidaum = img

    @img_vida2.setter
    def img_vida2(self, imagem):
        self.__img_vida2 = imagem

    @img_vida3.setter
    def img_vida3(self, imagem):
        self.__img_vida3 = imagem

    @pulando.setter
    def pulando(self, boolean):
        self.__pulando = boolean

    @agachado.setter
    def agachado(self, boolean):
        self.__agachado = boolean

    @colisao.setter
    def colisao(self, boolean):
        self.__colisao = boolean


    def desenha(self, screen):
        screen.blit(self.imagem, (self.cordenadas))
        screen.blit(self.__img_vida1, (0, 0))
        screen.blit(self.__img_vida2, (52, 0))
        screen.blit(self.__img_vida3, (104, 0))

    def atualizar(self):
        self.cordenadas[1] += self.velocidade

        if self.velocidade<= 11.1 and self.velocidade >= 10.9:
            self.__pulando = False     
            self.cordenadas[1] = 317

        if self.__pulando:
            self.velocidade = self.velocidade + self.__gravidade

        if self.velocidade <= 12.801 and self.velocidade >= 12.799:
            self.__pulando = False     
            self.cordenadas[1] = 317  

 
    def pular(self):
        self.__pulando = True
        self.velocidade = -12.8


            