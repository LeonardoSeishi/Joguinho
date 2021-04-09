import pygame
import math
pygame.init()


screen = pygame.display.set_mode((1200,500))

#title and icon

pygame.display.set_caption("jogo do dinossaurinho DO GOOGLE")
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

def player(player,x,y):
    screen.blit(player, (x, y))

def enemy(x,y):
    screen.blit(enemyimg, (x, y))

def isCollision(enemyX,enemyY,playerX,playerY):
    distancia = math.sqrt(((enemyX - playerX) **2) + ((enemyY - playerY)**2))
    if distancia < 70:
        return True
    else:
        return False



#game loop
running = True
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

    enemyX -=0.1

    

    player(playerimg_change,playerX,playerY)
    enemy(enemyX,enemyY)

    collision = isCollision(enemyX,enemyY,playerX,playerY)

    if collision:
        print('aaaaaaaaaaaaaa bateu')

    pygame.display.update()