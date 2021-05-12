import pygame
import json
#print(pygame.font.get_fonts())
class Menu():
    def __init__(self,jogo):
        self.jogo = jogo 
        self.meia_w, self.meia_h = 600,250
        self.rodar_display = True
        self.cursor_rect = pygame.Rect(0,0,150,150)
        self.offset = - 100
        self.screen = self.jogo.screen
        self.imagem_menu = 'imagens/background/imagem_menu.jpg'
        self.imgaux = pygame.image.load(self.imagem_menu).convert_alpha()
    def mostrar_cursor(self):
        self.jogo.desenha_texto('>', 20, self.cursor_rect.x, self.cursor_rect.y)
        

    def blit_screen(self,img):
        #self.jogo.screen.blit(self.jogo.display, (0, 0))
        pygame.display.update()
        self.jogo.screen.blit(img, (0, 0))
        #pygame.display.update()
        self.jogo.reset_keys()



class MainMenu(Menu):
    def __init__(self,jogo):
        Menu.__init__(self,jogo)
        self.state = 'Inicio'
        self.iniciox, self.inicioy = self.meia_w, self.meia_h -30
        self.pontuacaox, self.pontuacaoy = self.meia_w, self.meia_h + 70
        self.sairx, self.sairy = self.meia_w, self.meia_h + 200
        self.cursor_rect.midtop = (self.iniciox + self.offset, self.inicioy)
        

    def display_menu(self):
        self.rodar_display = True
        self.START_KEY = False
        while self.rodar_display:
            self.jogo.check_events()
            self.check_input()
            #self.jogo.display.fill(self.jogo.preto)
            self.jogo.desenha_texto('Start Game', 20, self.iniciox, self.inicioy)
            self.jogo.desenha_texto('Pontuacao', 20, self.pontuacaox, self.pontuacaoy)
            self.jogo.desenha_texto('Sair', 20, self.sairx, self.sairy)
            self.mostrar_cursor()  
            self.blit_screen(self.imgaux) 
            
    def move_cursor(self):
        #print(self.state)
        if self.jogo.DOWN_KEY:

            if self.state == 'Inicio':
                self.cursor_rect.midtop = (self.pontuacaox + self.offset, self.pontuacaoy)
                self.state = 'Pontuacao'
                #self.state = 'Pontuacao'

            elif self.state == 'Pontuacao':
                self.cursor_rect.midtop = (self.sairx + self.offset, self.sairy)
                self.state = 'Sair'

            elif self.state == 'Sair':
                self.cursor_rect.midtop = (self.iniciox + self.offset, self.inicioy)
                self.state = 'Inicio'

        if self.jogo.UP_KEY:
            if self.state == 'Inicio':
                self.cursor_rect.midtop = (self.sairx + self.offset, self.sairy)
                self.state = 'Sair'

            elif self.state == 'Pontuacao':
                self.cursor_rect.midtop = (self.iniciox + self.offset, self.inicioy)
                self.state = 'Inicio'

            elif self.state == 'Sair':
                self.cursor_rect.midtop = (self.pontuacaox + self.offset, self.pontuacaoy)
                self.state = 'Pontuacao'
               



    def check_input(self):
        self.move_cursor()
        if self.jogo.START_KEY:
            if self.state == 'Inicio':
                self.jogo.jogar()

            elif self.state == 'Pontuacao':
                self.jogo.set_curr_menu( self.jogo.menu_pontuacao) 

            elif self.state == 'Sair':
                self.rodar_display = False

            #self.rodar_display = False   

class MenuPontuacao(Menu):
    def __init__(self,jogo):
        Menu.__init__(self,jogo)
        self.arquivo = 'highscore.txt'
        self.data = {}
        self.state = 'Sair'
        self.sairx, self.sairy = self.meia_w, self.meia_h + 100
        self.cursor_rect.midtop = (self.sairx + self.offset, self.sairy)
        with open(self.arquivo) as score_file:
            self.data = json.load(score_file)
        self.string = (f'1 - {self.data["1"]} \n 2 - {self.data["2"]}\n 3 - {self.data["3"]}\n 4 - {self.data["4"]}\n5 - {self.data["5"]}\n')
        score_file.close()

    def display_menu(self):   
        self.rodar_display = True
        self.START_KEY = False
        while self.rodar_display:
            self.jogo.check_events()
            self.check_input()
            #self.jogo.display.fill((0,0,0))
            self.jogo.desenha_texto('SCORE BOARD', 20, 600, 100)
            self.jogo.desenha_texto(self.string, 10 , 600, 250)
            self.jogo.desenha_texto('Sair', 20, self.saidax, self.saiday)
            self.mostrar_cursor()  
            self.blit_screen(self.imgaux) 

    def move_cursor(self):
        if self.jogo.DOWN_KEY:
            if self.state == 'Sair':
                self.cursor_rect.midtop = (self.sairx + self.offset, self.sairy)
                self.state = 'Sair'
                

        if self.jogo.UP_KEY:
            if self.state == 'Sair':
                self.cursor_rect.midtop = (self.sairx + self.offset, self.sairy)
                self.state = 'Sair'

    def check_input(self):
        self.move_cursor()
        if self.jogo.START_KEY:
            if self.state == 'Sair':
                self.jogo.curr_menu = self.jogo.main_menu
                

class MenuFim(Menu):
    def __init__(self,jogo):
        Menu.__init__(self,jogo)
        self.state = 'Reiniciar'
        self.reinx, self.reiny = self.meia_w, self.meia_h
        self.saidax, self.saiday = self.meia_w, self.meia_h + 100
        self.cursor_rect.midtop = (self.reinx + self.offset, self.reiny)

    #def blit_screen_final(self):
        #pygame.display.update()
        #self.jogo.screen.blit(self.jogo.screen, (0, 0))
        #self.jogo.reset_keys()



    def display_menu(self):
        self.rodar_display = True
        self.START_KEY = False
        while self.rodar_display:
            self.jogo.check_events()
            self.check_input()
            #self.jogo.display.fill((0,0,0))
            self.jogo.desenha_texto('GAME OVER', 20, 600, 100)
            self.jogo.desenha_texto('Reiniciar', 20, self.reinx, self.reiny)
            self.jogo.desenha_texto('Sair', 20, self.saidax, self.saiday)
            self.mostrar_cursor()  
            self.blit_screen(self.jogo.screen) 
            

    
    def check_input(self):
        #print(self.state)
        #print(self.cursor_rect.x)
        #print(self.cursor_rect.y)
        if self.jogo.UP_KEY or self.jogo.DOWN_KEY:

            if self.state == 'Reiniciar':
                self.state = 'saida'
                self.cursor_rect.midtop = (self.saidax + self.offset , self.saiday)

            elif self.state == 'saida':
                self.state = 'Reiniciar'
                self.cursor_rect.midtop = (self.reinx + self.offset , self.reiny)


        if self.jogo.START_KEY:
            if self.state == 'Reiniciar':
                self.rodar_display = False
                self.jogo.jogar()

            if self.state == 'saida':
                self.rodar_display = False