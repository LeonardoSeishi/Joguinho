from abc import ABC, abstractmethod
from pygame.rect import Rect


class Objeto(ABC):

    def __init__(self, velocidade, x, y, img, largura, altura):
        self._cordenadas = [x, y]
        self._altura = altura
        self._largura = largura
        self._imagem = img
        self._velocidade = velocidade

        self.objRect = Rect(x, y, largura, altura)

    @abstractmethod
    def desenha(self, screen):
        screen.blit(self._imagem, (self._cordenadas[0], self._cordenadas[1]))

    @abstractmethod
    def atualizar(self):
        self._cordenadas[0] += self._velocidade
        if self._cordenadas[0] < 100:
            pass
