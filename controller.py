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
from menu import *

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

#dinossauro
dino_sprite = Spritesheet('imagens/jogador/dino_azul.png')
dino_sheet = [dino_sprite.parse_sprite('dino_azul0.png'),dino_sprite.parse_sprite('dino_azul1.png')]
dinoag_sprite = Spritesheet('imagens/jogador/dino_agachado.png')
dinoag_sheet = [dinoag_sprite.parse_sprite('dino_agachado0.png'),dinoag_sprite.parse_sprite('dino_agachado1.png')]
#obstaculos
cacto_sprite = Spritesheet('imagens/obstaculos/cactos.png')
cacto_sheet = [cacto_sprite.parse_sprite('cactos0.png'),cacto_sprite.parse_sprite('cactos1.png'),cacto_sprite.parse_sprite('cactos2.png')]
passaro_sprite = Spritesheet('imagens/obstaculos/passarinho.png')
passaro_sheet = [passaro_sprite.parse_sprite('passarinho0.png'),passaro_sprite.parse_sprite('passarinho1.png'),passaro_sprite.parse_sprite('passarinho2.png'),passaro_sprite.parse_sprite('passarinho3.png')]
#itens
moeda_sprite = Spritesheet('imagens/itens/Coin.png')
moeda_sheet = [moeda_sprite.parse_sprite('Coin0.png'),moeda_sprite.parse_sprite('Coin1.png'),moeda_sprite.parse_sprite('Coin2.png'),moeda_sprite.parse_sprite('Coin3.png'),moeda_sprite.parse_sprite('Coin4.png'),moeda_sprite.parse_sprite('Coin5.png'),moeda_sprite.parse_sprite('Coin6.png'),moeda_sprite.parse_sprite('Coin7.png'),moeda_sprite.parse_sprite('Coin8.png')]
mini_moeda_sprite = Spritesheet('imagens/itens/moeda_pequena.png')
mini_moeda_sheet = [mini_moeda_sprite.parse_sprite('moeda_pequena0.png'),mini_moeda_sprite.parse_sprite('moeda_pequena1.png'),mini_moeda_sprite.parse_sprite('moeda_pequena2.png'),mini_moeda_sprite.parse_sprite('moeda_pequena3.png')]
poderes = Spritesheet('imagens/itens/poderes.png')
poderes_sheet = [poderes.parse_sprite('poderes0.png'),poderes.parse_sprite('poderes1.png')]
moldura_sheet = [poderes.parse_sprite('poderes2.png'),poderes.parse_sprite('poderes3.png'),poderes.parse_sprite('poderes4.png'),poderes.parse_sprite('poderes5.png'),poderes.parse_sprite('poderes6.png'),poderes.parse_sprite('poderes7.png'),poderes.parse_sprite('poderes8.png'),poderes.parse_sprite('poderes9.png'),poderes.parse_sprite('poderes10.png'),poderes.parse_sprite('poderes11.png')]

#velocidade geral
velocidade = -9
velocidade_pulo = -17
gravidade = 0.6
aceleracao = -0.0002
# intanciando classes
#def reiniciar():
dino = Jogador(0, 80, 320, dino_sheet, 128, 120, gravidade, img_vida, poderes_sheet, moldura_sheet, velocidade_pulo)
cacto = Obstaculo(velocidade, 800, 350, cacto_sheet , 32, 96, aceleracao)
mapa = Background_controller(layers,velocidade, aceleracao)
moeda = Moeda(velocidade, 1000, 220, moeda_sheet, 48, 48, aceleracao)
mini_moeda = Moeda(0, 970, 25, mini_moeda_sheet, 32, 32, 0)
#passaro = Obstaculo(velocidade + 2, 800, --range(200,350), 96,96, aceleracao)

font = pygame.font.Font("imagens/fonte/PressStart2P-vav7.ttf", 30)
#font_lost = pygame.font.Font('freesansbold.ttf', 60)
pontuacao = Pontuacao()
branco = (255,255,255)
preto = (0,0,0)
#FPS
clock = pygame.time.Clock()
fps = 60

allObjects = [dino, cacto, moeda, mini_moeda]

class Menu_Controller():
    def __init__(self):
        pygame.init()
        self.display = pygame.Surface((1200,500))
        self.UP_KEY = False
        self.DOWN_KEY = False
        self.START_KEY = False
        self.BACK_KEY = False
        self.rodando = True     
        self.jogando = False
        self.screen = screen
        self.preto = preto
        self.main_menu = MainMenu(self)
        self.final_menu = MenuFim(self)
        self.curr_menu = self.main_menu

        if self.rodando:

            self.curr_menu.display_menu()
            self.reset_keys()
            pygame.display.update()
            #self.reset_keys()

    def desenha_texto(self,texto, tamanho, x, y):
        superficie_texto = font.render(texto, True, (0,0,0))
        text_rect = superficie_texto.get_rect()
        text_rect.center = (x,y)
        self.screen.blit(superficie_texto,text_rect)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.jogando = False
                self.curr_menu.rodar_display = False
                self.rodando = False

            if event.type == pygame.KEYDOWN:
                    if self.jogando: 
                        if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                            if (not dino.pulando and not dino.agachado) or dino.double_jump: 
                                dino.pular()

                    if event.key == pygame.K_RETURN:
                        self.START_KEY = True

                    if event.key == pygame.K_BACKSPACE:
                        self.BACK_KEY = True

                    if event.key == pygame.K_UP:
                        self.UP_KEY = True

                    if event.key == pygame.K_DOWN:
                        self.DOWN_KEY = True
                        dino.imagem = dinoag_sheet
                        dino.agachado = True
                        dino.altura = 76
                        dino.largura = 160

                    if event.key == pygame.K_LEFT:
                        if dino.num_moedas < 20:
                            dino.set_moldura_escudo(moldura_sheet[0])  
                        else:
                            if not dino.escudo:
                                dino.num_moedas -= 20
                            dino.escudo = True
                    
                    if event.key == pygame.K_RIGHT:
                        if dino.num_moedas < 10:
                            dino.set_moldura_double_jump(moldura_sheet[0])
                        else:
                            if not dino.double_jump:
                                dino.num_moedas -= 10
                            dino.double_jump = True
                                                 
                                                
            if event.type == pygame.KEYUP:
                    
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = False
                    dino.imagem = dino_sheet
                    dino.agachado = False
                    dino.altura = 120
                    dino.largura = 128

                if event.key == pygame.K_RETURN:
                    self.START_KEY = False

                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = False

                if event.key == pygame.K_UP:
                    self.UP_KEY = False

                if event.key == pygame.K_LEFT:
                    dino.set_moldura_escudo(moldura_sheet[1])

                if event.key == pygame.K_RIGHT:
                    dino.set_moldura_double_jump(moldura_sheet[1])


    def reset_keys(self):
        self.UP_KEY , self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False , False 


    def game_over(self):
        self.curr_menu = self.final_menu 
        self.jogando = False
        #self.rodando = True
        #dino = Jogador(0, 80, 320, dino_sheet, 128, 120, gravidade, img_vida, poderes_sheet, moldura_sheet, velocidade_pulo)
        #cacto = Obstaculo(velocidade, 800, 350, cacto_sheet , 32, 96, aceleracao)
        #mapa = Background_controller(layers,velocidade, aceleracao)
        #moeda = Moeda(velocidade, 1000, 220, moeda_sheet, 48, 48, aceleracao)
        #mini_moeda = Moeda(0, 970, 25, mini_moeda_sheet, 32, 32, 0)
        #passaro = Obstaculo(velocidade + 2, 800, --range(200,350), 96,96, aceleracao)
        #pontuacao.pontos = 0
        #self.curr_menu = self.final_menu        
        self.curr_menu.display_menu()
        #self.reset_keys()
        #pygame.display.update()
        
    def jogar(self):
        self.jogando = True
        self.rodando = False
        while self.jogando:
            self.check_events()
            
            if cacto.cordenadas[0] < -50:
                dino.colisao = False

            # colisao
            if dino.objRect.colliderect(cacto.objRect) and not dino.colisao:
                dino.colisao = True
                if not dino.escudo:
                    if dino.vidas == 3:
                        dino.set_img_vida3(img_notvida)
                    elif dino.vidas == 2:
                        dino.set_img_vida2(img_notvida)
                    elif dino.vidas == 1:
                        dino.set_img_vida1(img_notvida)
                    dino.vidas = dino.vidas - 1
                else:
                    dino.escudo = False
                    dino.set_moldura_escudo(moldura_sheet[1])
                

            if dino.objRect.colliderect(moeda.objRect):
                moeda.colisao = True
                dino.num_moedas += 1
                pontuacao.pontos = 75

            
            # game over
            #if dino.vidas == 0:
                #self.game_over()
                
                
                
                #self.inicia()

            # atualizar e desenhar
            mapa.loop(screen)
            for objeto in allObjects:
                objeto.atualizar()
                objeto.desenha(screen)
            pontuacao.contagem(screen)
            pontuacao.mostrar_moedas(screen,dino.num_moedas)

            pygame.display.update()

            # game over
            if dino.vidas == 0:
                self.jogando = False
                self.game_over()

            clock.tick(fps)

        

jogo = Menu_Controller()

