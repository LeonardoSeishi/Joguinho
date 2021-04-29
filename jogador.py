import pygame
from objeto import Objeto

class Jogador(Objeto):
    def __init__(self, velocidade, x, y, imagem, largura, altura, img_vida):
        super().__init__(velocidade, x, y, imagem, largura, altura)
        self.__vidas = 3
        self.__img_vida1 = img_vida
        self.__img_vida2 = img_vida
        self.__img_vida3 = img_vida
        self.__gravidade = 0.25
        self.__pulando = False
        self.__agachado = False
        self.__colisao = False

    def desenha(self, screen):
        screen.blit(self.__imagem, (self.__cordenadas[0], self.__cordenadas[1]))
        screen.blit(self.__img_vida1, (0, 0))
        screen.blit(self.__img_vida2, (52, 0))
        screen.blit(self.__img_vida3, (104, 0))

    def atualizar(self):
        self.__cordenadas[1] += self.__velocidade

        if self.__velocidade<= 11.1 and self.__velocidade >= 10.9:
            self.__pulando = False     
            self.__cordenadas[1] = 317

        if self.__pulando:
            self.__velocidade = self.__velocidade + self.__gravidade

        if self.__velocidade <= 12.801 and self.__velocidade >= 12.799:
            self.__pulando = False     
            self.__cordenadas[1] = 317  
 
    def pular(self):
        self.__pulando = True
        self.__velocidade = -12.8


            