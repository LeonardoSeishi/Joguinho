import pygame
import math
import PySimpleGUI as sg
from random import choice
import time
from pontuacao import Pontuacao
rodando = True
running = False
sg.theme('DarkAmber')
inside = [
            [sg.Text('',size = (5,1)),sg.Text('JOGUINHO',size=(14,1) )],
            [sg.Text('')],  
            [sg.Text('',size = (2,1)),sg.Button('INICIAR JOGO')],
            [sg.Text('',size = (2,1)),sg.Button('DIFICULDADE')],
            [sg.Text('',size = (2,1)),sg.Button('VER PONTUACAO')],
            [sg.Text('')],
            [sg.Text('',size = (6,1)),sg.Button('SAIR')]
         ]
janela = sg.Window('dinos',inside,font=("Helvetica", 37))


while rodando:
    event,values = janela.read()
    if event == sg.WIN_CLOSED:
        rodando = False
    elif event == "INICIAR JOGO":
        rodando = False
        running = True
    elif event == 'SAIR':
        rodando = False
janela.close()





pygame.init()


screen = pygame.display.set_mode((1200,500))

#title and icon and background

pygame.display.set_caption("jogo do dinossaurinho")
icon = pygame.image.load('dino.png')
pygame.display.set_icon(icon)
fundoimg = pygame.image.load('background_grande.png')
global pontos
pontos = 0
gravity = 0.4
aceleracao = 0.0005

#player
playerimg = pygame.image.load('dino_kawai_pe.png')
player_agach = pygame.image.load('dino_kawai.png')
playerX = 100
playerY = 317
playerY_change = 0
playerimg_change = playerimg
isJumping = False
vidas = 3
playerRect = pygame.Rect(playerX, playerY, 64, 64)

#enemy
enemyimg1 = pygame.image.load('cacto1.png')
enemyimg2 = pygame.image.load('cacto2.png')
enemyimg3 = pygame.image.load('cacto3.png')
cacto = [enemyimg1, enemyimg2, enemyimg3]
enemyX = 800
enemyY = 349
enemyY_change = 0
velocidade = 5
enemyRect = pygame.Rect(enemyX, enemyY, 40, 96)
isHit = False

#vida
vidaimg = pygame.image.load('vida.png')
vida_branca = pygame.image.load('vida_branca.png')
vidaX = 0
vidaY = 0
vidaX2 = 55
vidaX3 = 110
vidaimg_change = vidaimg
vidaimg_change2 = vidaimg
vidaimg_change3 = vidaimg

#pontuacao

font = pygame.font.Font('freesansbold.ttf', 20)
font_lost = pygame.font.Font('freesansbold.ttf', 60)

pontuacao = Pontuacao(screen)#pontuacao

def player(player,x,y):
    screen.blit(player, (x, y))

def fundo(x,y):
    screen.blit(fundoimg,(x,y))
def enemy(enemyimg,x,y):
    screen.blit(enemyimg, (x, y))

def vida(vidaimg, x,y):
    screen.blit(vidaimg,(x,y))

def isCollision(enemyX,enemyY,playerX,playerY):
    distancia = math.sqrt(((enemyX - playerX) **2) + ((enemyY - playerY)**2))
    if distancia < 75:
        return True
    else:
        return False



#game loop

while running:

    screen.fill((0,0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
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
        


    fundo(-200,0)
    vida(vidaimg_change,vidaX,vidaY)
    vida(vidaimg_change2,vidaX2,vidaY)
    vida(vidaimg_change3,vidaX3,vidaY)
    player(playerimg_change,playerX,playerY)
    enemy(enemyimg3, enemyX,enemyY)
    collision = isCollision(enemyX,enemyY,playerX,playerY)
    pontuacao.contagem()

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
        time.sleep(5)
        running = False

       
    pygame.display.update()