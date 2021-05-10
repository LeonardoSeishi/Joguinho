import pygame

class Menu():
    def __init__(self,jogo):
        self.jogo = jogo 
        self.meia_w, self.meia_h = 600,250
        self.rodar_display = True
        self.cursor_rect = pygame.Rect(0,0,150,150)
        self.offset = - 100

    
    def mostrar_cursor(self):
        self.jogo.desenha_texto('-', 20, self.cursor_rect.x, self.cursor_rect.y)


    def blit_screen(self):
        #self.jogo.screen.blit(self.jogo.display, (0, 0))
        pygame.display.update()
        self.jogo.screen.blit(self.jogo.display, (0, 0))
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
        while self.rodar_display:
            self.jogo.check_events()
            self.check_input()
            self.jogo.display.fill(self.jogo.preto)
            self.jogo.desenha_texto('Main Menu', 20, 600, 100)
            self.jogo.desenha_texto('Start Game', 20, self.iniciox, self.inicioy)
            self.jogo.desenha_texto('Pontuacao', 20, self.pontuacaox, self.pontuacaoy)
            self.jogo.desenha_texto('Sair', 20, self.sairx, self.sairy)
            self.mostrar_cursor()  
            self.blit_screen() 
            
    def move_cursor(self):
        print(self.state)
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
                pass

            elif self.state == 'Sair':
                pass

            self.rodar_display = False   


class MenuFim(Menu):
    def __init__(self,jogo):
        Menu.__init__(self,jogo)
        self.state = 'Reiniciar'
        self.reinx, self.reiny = self.meia_w, self.meia_h
        self.saidax, self.saiday = self.meia_w, self.meia_h + 100
        self.cursor_rect.midtop = (self.reinx + self.offset, self.reiny)

    def display_menu(self):
        self.rodar_display = True
        while self.rodar_display:
            self.jogo.check_events()
            self.check_input()
            self.jogo.display.fill((0,0,0))
            self.jogo.desenha_texto('GAME OVER', 20, 600, 100)
            self.jogo.desenha_texto('Reiniciar', 20, self.reinx, self.reiny)
            self.jogo.desenha_texto('Sair', 20, self.saidax, self.saiday)
            self.mostrar_cursor()  
            self.blit_screen() 
            

    
    def check_input(self):
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