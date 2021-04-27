from pygame.rect import Rect
import pygame
class Pontuacao():
    def __init__(self,screen):
        self.__screen = screen
        self.__pontos = 0
        self.__font = pygame.font.Font('freesansbold.ttf', 20)

    def contagem(self):
        self.__pontos += 1
        texto = self.__font.render('pontos: '+ str(self.__pontos), True, (0, 0, 0))
        texto_rect = texto.get_rect()
        texto_rect.center = (1100, 40)
        return self.__screen.blit(texto, texto_rect)