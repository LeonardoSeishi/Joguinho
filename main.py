import pygame

pygame.init()


screen = pygame.display.set_mode((1200,490))

#title and icon

pygame.display.set_caption("jogo do dinossaurinho DO GOOGLE")
icon = pygame.image.load('dino.png')
pygame.display.set_icon(icon)
#player

playerimg = pygame.image.load('dino_kawai.png')
playerX = 100
playerY = 426

def player():
    screen.blit(playerimg, (playerX, playerY))

#game loop
running = True
while running:

    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    player()
    pygame.display.update()