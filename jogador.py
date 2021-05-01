import pygame
from objeto import Objeto

class Jogador(Objeto):
    def __init__(self, velocidade, x, y, imagem, largura, altura, aceleracao, img_vida):
        super().__init__(velocidade, x, y, imagem, largura, altura, aceleracao)
        self.__vidas = 3
        self.__img_vida1 = img_vida
        self.__img_vida2 = img_vida
        self.__img_vida3 = img_vida
        self.__aceleracao = aceleracao
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

    @pulando.setter
    def pulando(self, boolean):
        self.__pulando = boolean

    @agachado.setter
    def agachado(self, boolean):
        self.__agachado = boolean

    @colisao.setter
    def colisao(self, boolean):
        self.__colisao = boolean

    def set_img_vida1(self, img):
        self.__img_vida1 = img

    def set_img_vida2(self, imagem):
        self.__img_vida2 = imagem

    def set_img_vida3(self, imagem):
        self.__img_vida3 = imagem

    def desenha(self, screen):
        screen.blit(self.imagem, (self.cordenadas))
        screen.blit(self.__img_vida1, (0, 0))
        screen.blit(self.__img_vida2, (52, 0))
        screen.blit(self.__img_vida3, (104, 0))

    def atualizar(self):
        self.cordenadas[1] += self.velocidade
        self.objRect = pygame.Rect(self.cordenadas[0], self.cordenadas[1], self.largura, self.altura)

        if self.__pulando:
            self.velocidade = self.velocidade + self.__aceleracao

        if self.cordenadas[1] + self.altura > 445:
            self.__pulando = False
            self.velocidade = 0     
            self.cordenadas[1] = 317

        if self.__agachado:
            if self.__pulando:
                self.cordenadas[1] += 10
            else:
                self.cordenadas[1] = 381
                self.objRect = pygame.Rect(self.cordenadas[0], (self.cordenadas[1]/2), self.largura, (self.altura/2))

 
    def pular(self):
        self.__pulando = True
        self.velocidade = -5.5


            