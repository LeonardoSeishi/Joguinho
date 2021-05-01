from objeto import Objeto
import pygame

class ObstaculoMovel(Objeto):
    def __init__(self, velocidade, x, y, imagem, largura, altura, aceleracao):
        super().__init__(velocidade, x, y, imagem, largura, altura, aceleracao)

    def atualizar(self):
        self.objRect = pygame.Rect(self.cordenadas[0], self.cordenadas[1], self.largura, self.altura)
        self.velocidade += self.aceleracao
        self.cordenadas[0] += self.velocidade
        if self.cordenadas[0] < -100:
            self.cordenadas[0] = 2700