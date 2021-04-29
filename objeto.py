from abc import ABC, abstractmethod
from pygame.rect import Rect


class Objeto(ABC):

    def __init__(self, velocidade, x, y, img, largura, altura):
        self.cordenadas = [x, y]
        self.altura = altura
        self.largura = largura
        self.imagem = img
        self.velocidade = velocidade

        self.objRect = Rect(x, y, largura, altura)

    @abstractmethod
    def desenha(self, screen):
        screen.blit(self.imagem, (self.cordenadas[0], self.cordenadas[1]))

    @abstractmethod
    def atualizar(self):
        self.__cordenadas[0] += self.__velocidade
        if self.__cordenadas[0] < 100:
            pass
