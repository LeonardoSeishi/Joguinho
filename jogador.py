import pygame
from objeto import Objeto

img_vida = pygame.image.load('vida.png')
img_notvida = pygame.image.load('vida_branca.png')

class Jogador(Objeto):
    def __init__(self,velocidade, x, y, imagem, largura, altura):
        super().__init__(imagem, x, y, largura, altura, velocidade)
        self.vidas = 3
        self.img_vida1 = img_vida
        self.img_vida2 = img_vida
        self.img_vida3 = img_vida
        self.gravidade = 0.25
        self.pulando = False
        self.agachado = False
        

    def desenha(self, screen):
        screen.blit(self.imagem, (self.cordenadas[0], self.cordenadas[1]))
        screen.blit(self.img_vida1, (0, 0))
        screen.blit(self.img_vida2, (52, 0))
        screen.blit(self.img_vida3, (104, 0))

    def atualizar(self):
        self.cordenadas[1] += self.velocidade

        if self.__velocidade<= 11.1 and self.velocidade >= 10.9:
            self.pulando = False     
            self.cordenadas[1] = 317

        if self.pulando:
            self.velocidade = self.velocidade + self.gravidade


            
    def pular(self):
        self.__pulando = True
        self.__velocidade = -11


            