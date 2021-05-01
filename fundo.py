from objeto import Objeto


class Background(Objeto):
    def __init__(self, velocidade, imagem, aceleracao):
        super().__init__(velocidade, 0, 0, imagem, 0, 0, aceleracao)
        self.objRect.bottom = 500
        self.__backLoop = Objeto(velocidade, 0, 0, imagem, 0, 0, aceleracao)
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
