from abc import ABC, abstractmethod
from pygame.rect import Rect


class Objeto(ABC):

    def __init__(self, velocidade, x, y, imagem, largura, altura):
        self.__cordenadas = [x, y]
        self.__altura = altura
        self.__largura = largura
        self.__imagem = imagem
        self.__velocidade = velocidade
        self.__objRect = Rect(x, y, largura, altura)

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
    def objRect(self):
        return self.__objRect

    @cordenadas.setter
    def cordenadas(self, cordenadas:list):
        self.__cordenadas = cordenadas

    @imagem.setter
    def imagem(self, imagem):
        self.__imagem = imagem

    @velocidade.setter
    def velocidade(self, velocidade):
        self.__velocidade = velocidade

    @abstractmethod
    def desenha(self, screen):
        screen.blit(self.__imagem, (self.__cordenadas[0], self.__cordenadas[1]))

    @abstractmethod
    def atualizar(self):
        self.__cordenadas[0] += self.__velocidade
        if self.__cordenadas[0] < 100:
            pass
