from pygame.rect import Rect

class Background():
    def __init__(self,velocidade, imagem):
        self.__imagem,self.__rect = load_image(imagem ,-1,-1,-1)
        self.__imagem1,self.__rect1 = load_image(imagem ,-1,-1,-1)
        self.__rect.bottom = 500
        self.__rect1.bottom = 500
        self.__rect1.left = self.__rect.right
        self.__velocidade = velocidade

    def draw(self):
        screen.blit(self.__imagem,self.__rect)
        screen.blit(self.__imagem1,self.__rect1)

    def update(self):
        self.rect.left += self.__velocidade
        self.rect1.left += self.__velocidade

        if self.rect.right < 0:
            self.rect.left = self.rect1.right

        elif self.rect1.right < 0:
            self.rect1.left = self.rect.right
