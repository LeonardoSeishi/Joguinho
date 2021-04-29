from pygame.rect import Rect

class Background():
    def __init__(self,velocidade, imagem):
        self.__imagem = imagem
        self.__rect = self.__imagem.get_rect()
        self.__imagem1 = imagem
        self.__rect1 = self.__imagem.get_rect()
        self.__rect.bottom = 500
        self.__rect1.bottom = 500
        self.__rect1.left = self.__rect.right
        self.__velocidade = velocidade

    def draw(self):
        screen.blit(self.__imagem,self.__rect)
        screen.blit(self.__imagem1,self.__rect1)

    def update(self):
        self.__rect.left += self.__velocidade
        self.__rect1.left += self.__velocidade

        if self.__rect.right < 0:
            self.__rect.left = self.__rect1.right

        elif self.__rect1.right < 0:
            self.__rect1.left = self.__rect.right
