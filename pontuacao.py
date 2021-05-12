from pygame.rect import Rect
import pygame
from os import path


class Pontuacao():
    def __init__(self):
        self.__pontos = 0
        self.__font = pygame.font.Font("imagens/fonte/PressStart2P-vav7.ttf", 12)
        self.__font_f = pygame.font.Font("imagens/fonte/PressStart2P-vav7.ttf", 15)
        self.__font_moeda = pygame.font.Font("imagens/fonte/PressStart2P-vav7.ttf", 10)
        self.__arquivo = 'highscore.txt'
        
    @property
    def pontos(self):
        return self.__pontos

    @pontos.setter
    def pontos(self, valor):
        self.__pontos += valor

    def contagem(self, screen):
        self.__pontos += 1
        texto = self.__font.render('pontos: '+ str(self.__pontos), True, (255, 255, 255))
        texto_rect = texto.get_rect()
        texto_rect.center = (1100, 40)
        return screen.blit(texto, texto_rect)

    def mostrar_pontuacao(self, screen):
        texto_f = self.__font_f.render('Pontuação final: ' + str(self.__pontos), True, (0,0,0))
        texto_f_rect = texto_f.get_rect()
        texto_f_rect.center = (550, 250)
        return screen.blit(texto_f,texto_f_rect)

    def mostrar_moedas(self, screen, num_moedas):
        texto_f = self.__font_moeda.render('' + str(int(num_moedas/2)), True, (255,255,255))
        texto_f_rect = texto_f.get_rect()
        texto_f_rect.center = (961,41) 
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

