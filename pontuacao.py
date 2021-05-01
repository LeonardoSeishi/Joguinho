from pygame.rect import Rect
import pygame
from os import path




class Pontuacao():
    def __init__(self):
        self.__pontos = 0
        self.__font = pygame.font.Font('freesansbold.ttf', 20)
        self.__font_f = pygame.font.Font('freesansbold.ttf', 40)
        self.__arquivo = 'highscore.txt'

    def contagem(self, screen):
        self.__pontos += 1
        texto = self.__font.render('pontos: '+ str(self.__pontos), True, (0, 0, 0))
        texto_rect = texto.get_rect()
        texto_rect.center = (1100, 40)
        return screen.blit(texto, texto_rect)

    def mostrar_pontuacao(self, screen):
        texto_f = self.__font_f.render('Pontuação final: ' + str(self.__pontos), True, (0,0,0))
        texto_f_rect = texto_f.get_rect()
        texto_f_rect.center = (550, 250)
        return screen.blit(texto_f,texto_f_rect)

    def pontuacao_final(self,pontos):
        with open(path.join(dir,self.__arquivo), 'w') as f:
            try:
                highscore = int(f.read())
            except:
                highscore = 0

        if pontos > highscore:
            highscore = pontos
            dir = path.dirname(__dirname__)
            with open(path.join(dir,self.__arquivo), 'w') as f:
                try:
                    highscore = int(f.read())
                except:
                    highscore = 0

