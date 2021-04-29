from abc import ABC, abstractmethod
from pygame.rect import Rect


class Objeto(ABC):

    def __init__(self, velocidade, x, y, img, largura, altura):
        self.__cordenadas = [x, y]
        self.__altura = altura
        self.__largura = largura
        self.__imagem = img
        self.__velocidade = velocidade

        self.objRect = Rect(x, y, largura, altura)

    @abstractmethod
    def desenha(self, screen):
        screen.blit(self.__imagem, (self.__cordenadas[0], self.__cordenadas[1]))

    @abstractmethod
    def atualizar(self):
        self.__cordenadas[0] += self.__velocidade
        if self.__cordenadas[0] < 100:
            pass
