import pygame
import math
import PySimpleGUI as sg

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

#title and icon

pygame.display.set_caption("jogo do dinossaurinho")
icon = pygame.image.load('dino.png')
pygame.display.set_icon(icon)

#player
playerimg = pygame.image.load('dino_kawai_pe.png')
player_agach = pygame.image.load('dino_kawai.png')
playerX = 100
playerY = 372
playerY_change = 0
playerimg_change = playerimg

#enemy
enemyimg = pygame.image.load('inimigo.png')
enemyX = 800
enemyY = 404
playerY_change = 0

#vida
vidaimg = pygame.image.load('vida.png')
vida_branca = pygame.image.load('vida_branca.png')
vidaX = 0
vidaY = 0
vidaimg_change = vidaimg
def player(player,x,y):
    screen.blit(player, (x, y))

def enemy(x,y):
    screen.blit(enemyimg, (x, y))

def vida(vidaimg, x,y):
    screen.blit(vidaimg,(x,y))

def isCollision(enemyX,enemyY,playerX,playerY):
    distancia = math.sqrt(((enemyX - playerX) **2) + ((enemyY - playerY)**2))
    if distancia < 70:
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
                 playerY_change = -0.2

            if event.key == pygame.K_UP:
                 playerY_change = 0.2

            if event.key == pygame.K_DOWN:
                playerimg_change = player_agach

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                playerY_change = 0
            
            if event.key == pygame.K_DOWN:
                playerimg_change = playerimg
            
            if event.key == pygame.K_UP:
                 playerY_change = 0

    playerY += playerY_change
    if playerY <=0:
        playerY = 0
    
    elif playerY >= 372:
        playerY = 372

    enemyX -=0.3

    

    player(playerimg_change,playerX,playerY)
    enemy(enemyX,enemyY)
    vida(vidaimg_change,vidaX,vidaY)
    collision = isCollision(enemyX,enemyY,playerX,playerY)

    if collision:
        vidaimg_change = vida_branca

        

    pygame.display.update()