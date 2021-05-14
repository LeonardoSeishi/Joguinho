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
        self.img_pontuacao = pygame.image.load('imagens/background/img_pontuacao.jpg').convert_alpha()
        self.img_game_over = pygame.image.load('imagens/background/img_game_over.jpg').convert_alpha() 
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
        #self.rodar_display = True
        self.jogo.START_KEY = False
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
                self.rodar_display = False

            elif self.state == 'Pontuacao':
                self.jogo.men_pontuacao()
                self.rodar_display = False

            elif self.state == 'Sair':
                self.rodar_display = False
                self.jogo.rodando = False
            #self.rodar_display = False   

class MenuPontuacao(Menu):
    def __init__(self,jogo):
        Menu.__init__(self,jogo)
        self.arquivo = 'highscore.txt'
        self.data = {}
        self.state = 'Sair'
        self.sairx, self.sairy = self.meia_w -340, self.meia_h + 170
        self.cursor_rect.midtop = (self.sairx + self.offset, self.sairy)
        with open(self.arquivo,'r') as score_file:
            self.data = json.load(score_file)
        self.string1 = (f'1 - {self.data["1"]}') 
        self.string2 = (f'2 - {self.data["2"]}')
        self.string3 = (f'3 - {self.data["3"]}')
        self.string4 = (f'4 - {self.data["4"]}')
        self.string5 = (f'5 - {self.data["5"]}')
        score_file.close()

    def display_menu(self):   
        #self.rodar_display = True
        self.jogo.START_KEY = False
        while self.rodar_display:
            self.jogo.check_events()
            self.check_input()
            #self.jogo.display.fill((0,0,0))
            #self.jogo.desenha_texto('SCORE BOARD', 20, 600, 100)
            self.jogo.desenha_texto(self.string1, 15 , 200, 150)
            self.jogo.desenha_texto(self.string2, 15 , 200, 200)
            self.jogo.desenha_texto(self.string3, 15 , 200, 250)
            self.jogo.desenha_texto(self.string4, 15 , 200, 300)
            self.jogo.desenha_texto(self.string5, 15 , 200, 350)
            self.jogo.desenha_texto('Sair', 20, self.sairx, self.sairy)
            self.mostrar_cursor()  
            self.blit_screen(self.img_pontuacao) 

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
                self.jogo.menu_inic()
                self.rodar_display = False
                
                

class MenuFim(Menu):
    def __init__(self,jogo):
        Menu.__init__(self,jogo)
        self.state = 'Reiniciar'
        self.reinx, self.reiny = self.meia_w, self.meia_h + 60
        self.saidax, self.saiday = self.meia_w, self.meia_h + 150
        self.cursor_rect.midtop = (self.reinx + self.offset, self.reiny)
        self.pontos = 0
    #def blit_screen_final(self):
        #pygame.display.update()
        #self.jogo.screen.blit(self.jogo.screen, (0, 0))
        #self.jogo.reset_keys()


    def pegar_pontos(self, ponto):
        self.pontos = ponto


    def display_menu(self):
        #self.rodar_display = True
        self.jogo.START_KEY = False
        #self.jogo.UP_KEY = False
        #self.jogo.DOWN_KEY = False
        while self.rodar_display:
            self.jogo.check_events()
            self.check_input()
            #self.jogo.display.fill((0,0,0))
            self.jogo.desenha_texto(f'pontuacao final: {self.pontos} pontos', 20, 600, 190)
            self.jogo.desenha_texto('Reiniciar', 20, self.reinx, self.reiny)
            self.jogo.desenha_texto('Voltar', 20, self.saidax, self.saiday)
            self.mostrar_cursor()  
            self.blit_screen(self.img_game_over) 
            

    
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
                self.jogo.menu_inic()
                self.rodar_display = False