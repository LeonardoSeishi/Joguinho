import pygame
import math
import PySimpleGUI as sg
import random
from interface import Menu
from pontuacao import Pontuacao
from jogador import Jogador
from obstaculo import Obstaculo
from fundo import Background
from mapa import Background_controller
from moeda import Moeda
from spritesheet import Spritesheet


# iniciando pygame
pygame.init()
screen = pygame.display.set_mode((1200,500))

# titulo e icone
pygame.display.set_caption("jogo do dinossaurinho")
icon = pygame.image.load('imagens/jogador/dino.png')
pygame.display.set_icon(icon)

# imagens
fundo1 = Background('imagens/background/chao_layer1.png')
fundo2 = Background('imagens/background/montanha_layer2.png')
fundo3 = Background('imagens/background/montanha_layer3.png')
fundo4 = Background('imagens/background/montanha_layer4.png')
fundo5 = Background('imagens/background/ceu_layer5.png')
layers = [fundo5,fundo4,fundo3,fundo2,fundo1]
img_vida = pygame.image.load('imagens/jogador/vida.png')
img_notvida = pygame.image.load('imagens/jogador/vida_branca.png')

#spritesheet
dino_sprite = Spritesheet('imagens/jogador/dino_azul.png')
dino_sheet = [dino_sprite.parse_sprite('dino_azul0.png'),dino_sprite.parse_sprite('dino_azul1.png')]
dinoag_sprite = Spritesheet('imagens/jogador/dino_agachado.png')
dinoag_sheet = [dinoag_sprite.parse_sprite('dino_agachado0.png'),dinoag_sprite.parse_sprite('dino_agachado1.png')]
cacto_sprite = Spritesheet('imagens/obstaculos/cactos.png')
cacto_sheet = [cacto_sprite.parse_sprite('cactos0.png'),cacto_sprite.parse_sprite('cactos1.png'),cacto_sprite.parse_sprite('cactos2.png')]
moeda_sprite = Spritesheet('imagens/itens/Coin.png')
moeda_sheet = [moeda_sprite.parse_sprite('Coin0.png'),moeda_sprite.parse_sprite('Coin1.png'),moeda_sprite.parse_sprite('Coin2.png'),moeda_sprite.parse_sprite('Coin3.png'),moeda_sprite.parse_sprite('Coin4.png'),moeda_sprite.parse_sprite('Coin5.png'),moeda_sprite.parse_sprite('Coin6.png'),moeda_sprite.parse_sprite('Coin7.png'),moeda_sprite.parse_sprite('Coin8.png')]
#velocidade geral
velocidade = -8
velocidade_pulo = -12
gravidade = 0.3
aceleracao = -0.0001
# intanciando classes
dino = Jogador(0, 80, 320, dino_sheet, 128, 120, gravidade, img_vida, velocidade_pulo)
cacto = Obstaculo(velocidade, 800, 350, cacto_sheet, 32, 96, aceleracao)
mapa = Background_controller(layers,velocidade, aceleracao)
moeda = Moeda(velocidade, 1000, 220, moeda_sheet, 48, 48, aceleracao)
#font = pygame.font.Font('freesansbold.ttf', 20)
#font_lost = pygame.font.Font('freesansbold.ttf', 60)
pontuacao = Pontuacao()

#FPS
clock = pygame.time.Clock()
fps = 60

allObjects = [mapa, dino, cacto, moeda]

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
                            dino.imagem = dinoag_sheet
                            dino.agachado = True
                            dino.altura = 76
                            dino.largura = 160
                            
                if event.type == pygame.KEYUP:
                    
                    if event.key == pygame.K_DOWN:
                        dino.imagem = dino_sheet
                        dino.agachado = False
                        dino.altura = 120
                        dino.largura = 128

                       
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

            if dino.objRect.colliderect(moeda.objRect):
                moeda.colisao = True

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
            clock.tick(fps)


jogo = Menu_Controller()
jogo.inicia()
