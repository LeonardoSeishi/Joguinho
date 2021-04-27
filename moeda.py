import pygame


class Moeda():
    def __init__(self, velocidade, x, y, imagem):
        self.__velocidade = velocidade
        self.__posicao = [x,y]
        self.__imagem = imagem

    def desenhar(self):
        screen.blit(self.__imagem,self.__posicao[0],self.__posicao[1])

    def atualizar(self):
        self.__posicao[0] += self.__velocidade

        if self.__posicao[0] < 100:
            pass

