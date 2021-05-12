from pygame.rect import Rect
import pygame
from os import path
import json

class Pontuacao():
    def __init__(self):
        self.__pontos = 0
        self.__font = pygame.font.Font("imagens/fonte/PressStart2P-vav7.ttf", 12)
        self.__font_f = pygame.font.Font("imagens/fonte/PressStart2P-vav7.ttf", 15)
        self.__font_moeda = pygame.font.Font("imagens/fonte/PressStart2P-vav7.ttf", 10)
        self.__arquivo = 'highscore.txt'
        self.__data = {}
        
    @property
    def pontos(self):
        return self.__pontos

    @pontos.setter
    def pontos(self, valor):
        self.__pontos += valor

    @property
    def data(self):
        return self.__data

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
        with open(self.__arquivo) as score_file:
            self.__data = json.load(score_file)
        #print(pontos)
        for i in self.__data:
            
            if pontos > (self.__data[i]):
                if i == '1':
                    self.__data['5'] = self.__data['4']
                    self.__data['4'] = self.__data['3']
                    self.__data['3'] = self.__data['2']
                    self.__data['2'] = self.__data['1']
                    self.__data['1'] = pontos
                    break

                if i == '2':
                    self.__data['5'] = self.__data['4']
                    self.__data['4'] = self.__data['3']
                    self.__data['3'] = self.__data['2']
                    self.__data['2'] = pontos
                    break
                if i == '3':
                    self.__data['5'] = self.__data['4']
                    self.__data['4'] = self.__data['3']
                    self.__data['3'] = pontos
                    break
                if i =='4':
                    self.__data['5'] = self.__data['4']
                    self.__data['4'] = pontos
                    break
                if i==5:
                    self.__data['5'] = pontos
                    break
                    
        
        score_file.close()            
        print(self.__data)            
        with open (self.__arquivo,'w') as score_file:
            json.dump(self.__data, score_file)

        score_file.close()
