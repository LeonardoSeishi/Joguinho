from objeto import Objeto
import pygame


class Background(Objeto):
    def __init__(self, velocidade, imagem, aceleracao):
        imgaux = pygame.image.load(imagem).convert_alpha()
        super().__init__(velocidade, 0, 0, [imgaux], 0, 0, aceleracao)
        self.objRect.bottom = 500
        self.__backLoop = Objeto(velocidade, 0, 0, [imgaux], 0, 0, aceleracao)
        self.__backLoop.objRect.bottom = 500
        self.__backLoop.objRect.left = self.objRect.right

    def desenha(self, screen):
        super().desenha(screen)
        self.__backLoop.desenha(screen)

    def atualizar(self):
        self.velocidade += self.aceleracao
        self.__backLoop.velocidade += self.__backLoop.aceleracao
        self.objRect.left += self.velocidade
        self.__backLoop.objRect.left += self.__backLoop.velocidade

        if self.objRect.right < 0:
            self.objRect.left = self.__backLoop.objRect.right

        if self.__backLoop.objRect.right < 0:
            self.__backLoop.objRect.left = self.objRect.right
