import pygame
import math
import PySimpleGUI as sg
import random
from interface import Menu
from pontuacao import Pontuacao
from jogador import Jogador
from obstaculo import Obstaculo

#imagens
chao = pygame.image.load('chao_layer1.png')
montanha1 = pygame.image.load('montanha_layer2.png')
montanha2 = pygame.image.load('montanha_layer3.png')
montanha3 = pygame.image.load('montanha_layer4.png')
ceu = pygame.image.load('ceu_layer5.png')

img_jogador = pygame.image.load('dino_kawai_pe.png')
img_jogador_agachado = pygame.image.load('dino_kawai.png')

img_cacto1 = pygame.image.load('cacto1.png')
img_cacto2 = pygame.image.load('cacto2.png')
img_cacto3 = pygame.image.load('cacto3.png')



class Menu_Controller:
    def __init__(self, screen):
        self.__screen = screen
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

            self.__screen.fill((0,0,0))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__jogando = False
                    self.inicia()
                
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_SPACE:
                        if not isJumping: 
                            isJumping = True
                            playerY_change = -12.8

                    if event.key == pygame.K_DOWN:
                        playerimg_change = player_agach
                        

                if event.type == pygame.KEYUP:
                    
                    if event.key == pygame.K_DOWN:
                        playerimg_change = playerimg
                    
                    if event.key == pygame.K_UP:
                        playerY_change = 0

            if playerY_change <= 12.801 and playerY_change >= 12.799:
                isJumping = False     
                playerY = 317        

            if isJumping:
                playerY_change = playerY_change + gravity
                
                
            velocidade += aceleracao
            playerY += playerY_change
            enemyX -= velocidade
            playerRect.move(playerX, playerY)
            playerRect.x = playerX
            playerRect.y = playerY
            # enemyRect.move_ip(enemyX, enemyY)
            enemyRect.x = enemyX
            enemyRect.y = enemyY
            

            if enemyX < -100:
                isHit = False
                enemyX = 1250
                


            #fundo(-200,0)
            #vida(vidaimg_change,vidaX,vidaY)
            #vida(vidaimg_change2,vidaX2,vidaY)
            #vida(vidaimg_change3,vidaX3,vidaY)
            #player(playerimg_change,playerX,playerY)
            #enemy(enemyimg3, enemyX,enemyY)
            #collision = isCollision(enemyX,enemyY,playerX,playerY)
            #pontuacao.contagem()

            #pontuacao.mostrar_pontuacao() #mostra pontuacao

            if playerRect.colliderect(enemyRect) and not isHit:
                isHit = True
                if vidas == 3:
                    vidaimg_change3 = vida_branca
                elif vidas == 2:
                    vidaimg_change2 = vida_branca
                elif vidas == 1:
                    vidaimg_change = vida_branca
                vidas = vidas - 1

            if vidas == 0:
                self.__jogando = False
                self.inicia()

            
            pygame.display.update()



   