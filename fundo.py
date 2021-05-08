from objeto import Objeto
import pygame


class Background(Objeto):
    def __init__(self, imagem):
        imgaux = pygame.image.load(imagem).convert_alpha()
        super().__init__(0, 0, 0, [imgaux], 3500, 500, 0)
        self.objRect.bottom = 500
        self.__backLoop = Objeto(0, 0, 0, [imgaux], 3500, 500, 0)
        self.__backLoop.objRect.bottom = 500
        self.objRect.right = self.__backLoop.objRect.left


    def desenha(self, screen):
        super().desenha(screen)
        self.__backLoop.desenha(screen)

    def atualizar(self):
        self.velocidade += self.aceleracao
        self.objRect.left += self.velocidade
        self.__backLoop.objRect.left += self.velocidade

        if self.objRect.right < -10:
            self.objRect.left = self.__backLoop.objRect.right

        if self.__backLoop.objRect.right < -10:
            self.__backLoop.objRect.left = self.objRect.right
