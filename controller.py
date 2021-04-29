import pygame
import math
import PySimpleGUI as sg
import random
from interface import Menu
from pontuacao import Pontuacao
from jogador import Jogador
from obstaculo import Obstaculo
from fundo import Background

#iniciando pygame
pygame.init()
screen = pygame.display.set_mode((1200,500))

#titulo e icone
pygame.display.set_caption("jogo do dinossaurinho")
icon = pygame.image.load('dino.png')
pygame.display.set_icon(icon)

#imagens
chao = pygame.image.load('chao_layer1.png')
montanha1 = pygame.image.load('montanha_layer2.png')
montanha2 = pygame.image.load('montanha_layer3.png')
montanha3 = pygame.image.load('montanha_layer4.png')
ceu = pygame.image.load('ceu_layer5.png')

img_jogador = pygame.image.load('dino_kawai_pe.png')
img_jogador_agachado = pygame.image.load('dino_kawai.png')

img_vida = pygame.image.load('vida.png')
img_notvida = pygame.image.load('vida_branca.png')

img_cacto1 = pygame.image.load('cacto1.png')
img_cacto2 = pygame.image.load('cacto2.png')
img_cacto3 = pygame.image.load('cacto3.png')

#intanciando classes
dino = Jogador(0, 80, 317, img_jogador, 128, 112, img_vida)
cacto = Obstaculo(-5, 800, 345, img_cacto1, 40, 96)
fundo1 = Background(-5, chao)
fundo2 = Background(-1.5, montanha1)
fundo3 = Background(-1, montanha2)
fundo4 = Background(-0.5, montanha3)
fundo5 = Background(-0.01, ceu)
#font = pygame.font.Font('freesansbold.ttf', 20)
#font_lost = pygame.font.Font('freesansbold.ttf', 60)
pontuacao = Pontuacao(screen)

class Menu_Controller():
    def __init__(self):
        self.__tela_inicial = Menu()
        self.__rodando = True
        self.__jogando =  False

    def inicia(self):
        self.__tela_inicial.tela_consulta()

        while self.__rodando:
            event, values = self.__tela_inicial.le_eventos()

            if event == sg.WIN_CLOSED:
                self.__rodando = False

            elif event == 'INICIAR JOGO':
                self.__rodando = False
                self.__jogando = True
                self.jogar()

            elif event == 'DIFICULDADE':
                #abrir interface de dificuldades
                print("'-'")

            elif event == 'VER PONTUACAO':
                #abrir interface de pontuação
                print("'-'")
                
            elif event == 'SAIR':
                self.__rodando = False

        self.__tela_inicial.fim()
 
    def jogar(self):

        while self.__jogando:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__jogando = False
                    self.inicia()
                
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_SPACE:
                        if not dino.pulando: 
                            dino.pular()

                    if event.key == pygame.K_DOWN:
                       dino.imagem = img_jogador_agachado
                        
                if event.type == pygame.KEYUP:
                    
                    if event.key == pygame.K_DOWN:
                        dino.imagem = img_jogador
                       
            if cacto.cordenadas[0] < -100:
                dino.colisao = False

            #colisao
            if dino.objRect.colliderect(cacto.objRect) and not dino.colisao:
                dino.colisao = True
                if dino.vida == 3:
                    dino.img_vida3 = img_notvida
                elif dino.vida == 2:
                    dino.img_vida2 = img_notvida
                elif dino.vida == 1:
                    dino.img_vida1 = img_notvida
                dino.vida = dino.vida - 1

            #game over
            if dino.vidas == 0:
                self.__jogando = False
                self.inicia()

            #desenhar
            fundo5.desenha(screen)
            fundo4.desenha(screen)
            fundo3.desenha(screen)
            fundo2.desenha(screen)
            fundo1.desenha(screen)
            dino.desenha(screen)
            cacto.desenha(screen)
            pontuacao.contagem()
            #atualizar
            fundo5.atualizar()
            fundo4.atualizar()
            fundo3.atualizar()
            fundo2.atualizar()
            fundo1.atualizar()
            dino.atualizar()
            cacto.atualizar()            
            pygame.display.update()

jogo = Menu_Controller()
jogo.inicia()