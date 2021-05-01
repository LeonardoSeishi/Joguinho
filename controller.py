import pygame
import math
import PySimpleGUI as sg
import random
from interface import Menu
from pontuacao import Pontuacao
from jogador import Jogador
from obstaculo import Obstaculo
from obstaculo_movel import ObstaculoMovel
from fundo import Background

# iniciando pygame
pygame.init()
screen = pygame.display.set_mode((1200,500))

# titulo e icone
pygame.display.set_caption("jogo do dinossaurinho")
icon = pygame.image.load('imagens/jogador/dino.png')
pygame.display.set_icon(icon)

# imagens
chao = 'imagens/background/chao_layer1.png'
montanha1 = 'imagens/background/montanha_layer2.png'
montanha2 = 'imagens/background/montanha_layer3.png'
montanha3 = 'imagens/background/montanha_layer4.png'
ceu = 'imagens/background/ceu_layer5.png'

img_jogador = 'imagens/jogador/dino_kawai_pe.png'
img_jogador_agachado = 'imagens/jogador/dino_kawai.png'

img_vida = pygame.image.load('imagens/jogador/vida.png')
img_notvida = pygame.image.load('imagens/jogador/vida_branca.png')

img_cacto1 = 'imagens/obstaculos/cacto1.png'
img_cacto2 = 'imagens/obstaculos/cacto2.png'
img_cacto3 = 'imagens/obstaculos/cacto3.png'

#velocidade geral
velocidade = -1
gravidade = 0.05
aceleracao = -0.0001
# intanciando classes
dino = Jogador(0, 80, 317, img_jogador, 128, 128, gravidade, img_vida)
cacto = Obstaculo(velocidade, 800, 345, img_cacto1, 32, 96, aceleracao)
fundo1 = Background(velocidade, chao, aceleracao)
fundo2 = Background(-0.3, montanha1, 0)
fundo3 = Background(-0.2, montanha2, 0)
fundo4 = Background(-0.1, montanha3, 0)
fundo5 = Background(-0.04, ceu, 0)
#font = pygame.font.Font('freesansbold.ttf', 20)
#font_lost = pygame.font.Font('freesansbold.ttf', 60)
pontuacao = Pontuacao()

allObjects = [fundo5, fundo4, fundo3, fundo2, fundo1, dino, cacto,]

class Menu_Controller():
    def __init__(self):
        self.__tela_inicial = Menu()
        self.__rodando = True
        self.__jogando = False

    def inicia(self):
        self.__tela_inicial.tela_consulta()

        while self.__rodando:
            event, values = self.__tela_inicial.le_eventos()

            if event == sg.WIN_CLOSED:
                self.__rodando = False

            elif event == 'INICIAR JOGO':
                self.__rodando = False
                self.__jogando = True
                self.__tela_inicial.fim()
                self.jogar()

            elif event == 'DIFICULDADE':
                # abrir interface de dificuldades
                print("'-'")

            elif event == 'VER PONTUACAO':
                # abrir interface de pontuação
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
                        if not dino.pulando and not dino.agachado: 
                            dino.pular()

                    if event.key == pygame.K_DOWN:
                            dino.imagem = img_jogador_agachado
                            dino.agachado = True
                            
                if event.type == pygame.KEYUP:
                    
                    if event.key == pygame.K_DOWN:
                        dino.imagem = img_jogador
                        dino.agachado = False
                       
            if cacto.cordenadas[0] < -50:
                dino.colisao = False

            # colisao
            if dino.objRect.colliderect(cacto.objRect) and not dino.colisao:
                dino.colisao = True
                if dino.vidas == 3:
                    dino.set_img_vida3(img_notvida)
                elif dino.vidas == 2:
                    dino.set_img_vida2(img_notvida)
                elif dino.vidas == 1:
                    dino.set_img_vida1(img_notvida)
                dino.vidas = dino.vidas - 1

            # game over
            if dino.vidas == 0:
                self.__jogando = False
                self.inicia()

            # atualizar e desenhar
            for objeto in allObjects:
                objeto.atualizar()
                objeto.desenha(screen)
            pontuacao.contagem(screen)


            pygame.display.update()


jogo = Menu_Controller()
jogo.inicia()
