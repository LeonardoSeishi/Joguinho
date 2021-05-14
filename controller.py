import random

from fundo import Background
from gerador import Gerador
from jogador import Jogador
from mapa import Background_controller
from menu import *
from moeda import Moeda
from obstaculo import Obstaculo
from pontuacao import Pontuacao
from spritesheet import Spritesheet


# iniciando pygame
# titulo e icone
pygame.init()
screen = pygame.display.set_mode((1200,500))
pygame.display.set_caption("jogo do dinossaurinho")
icon = pygame.image.load('imagens/jogador/dino.png')
pygame.display.set_icon(icon)


class Menu_Controller():
    def __init__(self):
        pygame.init()
        self.v = Variaveis()
        self.pontuacao = Pontuacao()
        self.display = pygame.Surface((1200,500))
        self.UP_KEY = False
        self.DOWN_KEY = False
        self.START_KEY = False
        self.BACK_KEY = False
        self.rodando = True     
        self.jogando = False
        self.screen = screen
        self.preto = self.v.preto
        self.menu_pontuacao = MenuPontuacao(self)
        self.main_menu = MainMenu(self)
        self.final_menu = MenuFim(self)
        self.curr_menu = self.main_menu
        self.curr_menu.rodar_display = True
        def random_y():
            return random.randint(150, 280)
        self.gerador = Gerador(screen, entidades=[(Obstaculo, (self.v.velocidade, 2000, 350, self.v.cacto_sheet, 32, 96, self.v.aceleracao), 50),
                                                  (Obstaculo, (self.v.velocidade - 2, 2500, random_y, self.v.passaro_preto_sheet, 48, 48, self.v.aceleracao), 20),
                                                  (Moeda, (self.v.velocidade, 1500, 220, self.v.moeda_sheet, 48, 48, self.v.aceleracao), 0)], coeficiente_geracao=6)
        self.new_objects = []
        self.timer_colisao = 0
        self.total_frames = 0
    


    def desenha_texto(self,texto, tamanho, x, y):
        superficie_texto = self.v.font.render(texto, True, (0,0,0))
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
                            if (not self.v.dino.pulando and not self.v.dino.agachado) or self.v.dino.double_jump:
                                self.v.dino.pular()

                    if event.key == pygame.K_RETURN:
                        self.START_KEY = True

                    if event.key == pygame.K_BACKSPACE:
                        self.BACK_KEY = True

                    if event.key == pygame.K_UP:
                        self.UP_KEY = True

                    if event.key == pygame.K_DOWN:
                        self.DOWN_KEY = True
                        self.v.dino.imagem = self.v.dinoag_sheet
                        self.v.dino.agachado = True
                        self.v.dino.altura = 76
                        self.v.dino.largura = 160

                    if event.key == pygame.K_LEFT:
                        if self.v.dino.num_moedas < 10:
                            self.v.dino.set_moldura_escudo(self.v.moldura_sheet[0])
                        else:
                            if not self.v.dino.escudo:
                                self.v.dino.num_moedas -= 10
                            self.v.dino.escudo = True
                    
                    if event.key == pygame.K_RIGHT:
                        if self.v.dino.num_moedas < 5:
                            self.v.dino.set_moldura_double_jump(self.v.moldura_sheet[0])
                        else:
                            if not self.v.dino.double_jump:
                                self.v.dino.num_moedas -= 5
                            self.v.dino.double_jump = True
                                                 
                                                
            if event.type == pygame.KEYUP:
                    
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = False
                    self.v.dino.imagem = self.v.dino_sheet
                    self.v.dino.agachado = False
                    self.v.dino.altura = 120
                    self.v.dino.largura = 128

                if event.key == pygame.K_RETURN:
                    self.START_KEY = False

                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = False

                if event.key == pygame.K_UP:
                    self.UP_KEY = False

                if event.key == pygame.K_LEFT:
                    self.v.dino.set_moldura_escudo(self.v.moldura_sheet[1])

                if event.key == pygame.K_RIGHT:
                    self.v.dino.set_moldura_double_jump(self.v.moldura_sheet[1])


    def reset_keys(self):
        self.UP_KEY , self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False , False 


    def game_over(self):
        self.pontuacao.pontuacao_final(self.pontuacao.pontos)
        self.menu_pontuacao = MenuPontuacao(self)
        self.curr_menu = self.final_menu
        self.curr_menu.pegar_pontos(self.pontuacao.pontos)
        self.jogando = False
        self.rodando = True
        self.reset_keys()
        pygame.display.update()
        self.curr_menu.rodar_display = True
        self.v = Variaveis()
        self.pontuacao = Pontuacao()

    def men_pontuacao(self):
        self.curr_menu = self.menu_pontuacao
        pygame.display.update()
        self.curr_menu.rodar_display = True

    def menu_inic(self):
        self.curr_menu = self.main_menu
        pygame.display.update()
        self.curr_menu.rodar_display = True
        
    def jogar(self):
        pygame.mixer.music.load('sons/musica/musica1_teste.mp3')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
        self.jogando = True
        self.rodando = False
        while self.jogando:
            self.check_events()

            if self.v.dino.colisao:
                self.timer_colisao += 1
            if self.timer_colisao > 100:
                self.v.dino.colisao = False
                self.timer_colisao = 0

            #poder
            if self.v.dino.agachado:
                if self.v.dino.double_jump and self.v.dino.escudo:
                    self.v.dino.imagem = self.v.dinoag_bota_escudo
                elif self.v.dino.double_jump:
                    self.v.dino.imagem = self.v.dinoag_bota
                elif self.v.dino.escudo:
                    self.v.dino.imagem = self.v.dinoag_escudo
                else:
                    self.v.dino.imagem = self.v.dinoag_sheet
            else:
                if self.v.dino.double_jump and self.v.dino.escudo:
                    self.v.dino.imagem = self.v.dino_bota_escudo
                elif self.v.dino.double_jump:
                    self.v.dino.imagem = self.v.dino_bota
                elif self.v.dino.escudo:
                    self.v.dino.imagem = self.v.dino_escudo
                else:
                    self.v.dino.imagem = self.v.dino_sheet

            # colisao
            for objeto in self.v.allObjects:
                if self.v.dino.objRect.colliderect(objeto.objRect):
                    if isinstance(objeto, Obstaculo) and not self.v.dino.colisao:
                        self.v.danoSound.play()
                        self.v.dino.colisao = True
                        if not self.v.dino.escudo:
                            self.v.dino.vidas = 0
                            # if dino.vidas == 3:
                            #     dino.set_img_vida3(img_notvida)
                            # elif dino.vidas == 2:
                            #     dino.set_img_vida2(img_notvida)
                            # elif dino.vidas == 1:
                            #     dino.set_img_vida1(img_notvida)
                            # dino.vidas = dino.vidas - 1
                        else:
                            self.v.dino.escudo = False
                            self.v.dino.set_moldura_escudo(self.v.moldura_sheet[1])
                    elif isinstance(objeto, Moeda):
                        self.v.moedaSound.play()
                        objeto.colisao = True
                        self.v.dino.num_moedas += 1
                        self.pontuacao.pontos = 75
                        objeto.cordenadas[0] = -100

            # atualizar e desenhar
            self.v.mapa.loop(screen)

            self.total_frames += 1
            # print(f'Todos Objetos {len(allObjects)}\nNovos Objetos {len(self.new_objects)}')
            for new_object in self.new_objects:
                new_object.velocidade += self.v.aceleracao * self.total_frames
                self.v.allObjects.append(new_object)
                self.new_objects.remove(new_object)
            to_remove_list = []

            for objeto in self.v.allObjects:
                objeto.atualizar()
                objeto.desenha(screen)
                if objeto.cordenadas[0] < -100:
                    to_remove_list.append(objeto)
                    # allObjects.remove(objeto)
            for to_remove in to_remove_list:
                self.v.allObjects.remove(to_remove)
            obj = self.gerador.atualizar(self.v.allObjects)
            if obj is not None:
                self.new_objects.append(obj)

            self.v.mini_moeda.atualizar()
            self.v. mini_moeda.desenha(screen)
            self.pontuacao.contagem(screen)
            self.pontuacao.mostrar_moedas(screen, self.v.dino.num_moedas)
            pygame.display.flip()

            # game over
            if self.v.dino.vidas == 0:
                self.jogando = False
                self.rodando = True
                self.game_over()

            self.v.clock.tick(self.v.fps)
        pygame.mixer.music.fadeout(2000)
        self.v.gameOverSound.play()


class Variaveis:
    def __init__(self):
        # imagens
        self.fundo1 = Background('imagens/background/chao_layer1.png')
        self.fundo2 = Background('imagens/background/montanha_layer2.png')
        self.fundo3 = Background('imagens/background/montanha_layer3.png')
        self.fundo4 = Background('imagens/background/montanha_layer4.png')
        self.fundo5 = Background('imagens/background/ceu_layer5.png')
        self.layers = [self.fundo5, self.fundo4, self.fundo3, self.fundo2, self.fundo1]
        self.img_vida = pygame.image.load('imagens/jogador/vida.png')
        self.img_notvida = pygame.image.load('imagens/jogador/vida_branca.png')

        # spritesheet

        # dinossauro
        self.dino_sprite = Spritesheet('imagens/jogador/dino_azul.png')
        self.dino_sheet = [self.dino_sprite.parse_sprite('dino_azul0.png'), self.dino_sprite.parse_sprite('dino_azul1.png')]
        self.dino_escudo = [self.dino_sprite.parse_sprite('dino_azul2.png'), self.dino_sprite.parse_sprite('dino_azul3.png')]
        self.dino_bota = [self.dino_sprite.parse_sprite('dino_azul4.png'), self.dino_sprite.parse_sprite('dino_azul5.png')]
        self.dino_bota_escudo = [self.dino_sprite.parse_sprite('dino_azul6.png'), self.dino_sprite.parse_sprite('dino_azul7.png')]
        self.dinoag_sprite = Spritesheet('imagens/jogador/dino_agachado.png')
        self.dinoag_sheet = [self.dinoag_sprite.parse_sprite('dino_agachado0.png'),
                        self.dinoag_sprite.parse_sprite('dino_agachado1.png')]
        self.dinoag_bota = [self.dinoag_sprite.parse_sprite('dino_agachado2.png'),
                       self.dinoag_sprite.parse_sprite('dino_agachado3.png')]
        self.dinoag_escudo = [self.dinoag_sprite.parse_sprite('dino_agachado4.png'),
                         self.dinoag_sprite.parse_sprite('dino_agachado5.png')]
        self.dinoag_bota_escudo = [self.dinoag_sprite.parse_sprite('dino_agachado6.png'),
                              self.dinoag_sprite.parse_sprite('dino_agachado7.png')]
        # obstaculos
        self.cacto_sprite = Spritesheet('imagens/obstaculos/cactos.png')
        self.cacto_sheet = [self.cacto_sprite.parse_sprite('cactos0.png'), self.cacto_sprite.parse_sprite('cactos1.png'),
                       self.cacto_sprite.parse_sprite('cactos2.png')]
        self.passaro_sprite = Spritesheet('imagens/obstaculos/passarinho.png')
        self.passaro_preto_sheet = [self.passaro_sprite.parse_sprite('passarinho0.png'),
                               self.passaro_sprite.parse_sprite('passarinho1.png')]
        self.passaro_marrom_sheet = [self.passaro_sprite.parse_sprite('passarinho2.png'),
                                self.passaro_sprite.parse_sprite('passarinho3.png')]
        # itens
        self.moeda_sprite = Spritesheet('imagens/itens/Coin.png')
        self.moeda_sheet = [self.moeda_sprite.parse_sprite('Coin0.png'), self.moeda_sprite.parse_sprite('Coin1.png'),
                       self.moeda_sprite.parse_sprite('Coin2.png'), self.moeda_sprite.parse_sprite('Coin3.png'),
                       self.moeda_sprite.parse_sprite('Coin4.png'), self.moeda_sprite.parse_sprite('Coin5.png'),
                       self.moeda_sprite.parse_sprite('Coin6.png'), self.moeda_sprite.parse_sprite('Coin7.png'),
                       self.moeda_sprite.parse_sprite('Coin8.png')]
        self.mini_moeda_sprite = Spritesheet('imagens/itens/moeda_pequena.png')
        self.mini_moeda_sheet = [self.mini_moeda_sprite.parse_sprite('moeda_pequena0.png'),
                            self.mini_moeda_sprite.parse_sprite('moeda_pequena1.png'),
                            self.mini_moeda_sprite.parse_sprite('moeda_pequena2.png'),
                            self.mini_moeda_sprite.parse_sprite('moeda_pequena3.png')]
        self.poderes = Spritesheet('imagens/itens/poderes.png')
        self.poderes_sheet = [self.poderes.parse_sprite('poderes0.png'), self.poderes.parse_sprite('poderes1.png')]
        self.moldura_sheet = [self.poderes.parse_sprite('poderes2.png'), self.poderes.parse_sprite('poderes3.png'),
                         self.poderes.parse_sprite('poderes4.png'), self.poderes.parse_sprite('poderes5.png'),
                         self.poderes.parse_sprite('poderes6.png'), self.poderes.parse_sprite('poderes7.png'),
                         self.poderes.parse_sprite('poderes8.png'), self.poderes.parse_sprite('poderes9.png'),
                         self.poderes.parse_sprite('poderes10.png'),self.poderes.parse_sprite('poderes11.png')]

        # velocidade geral
        self.velocidade = -9
        self.velocidade_pulo = -17
        self.gravidade = 0.6
        self.aceleracao = -0.0002
        # intanciando classes
        # def reiniciar():
        self.dino = Jogador(0, 80, 320, self.dino_sheet, 128, 120, self.gravidade, self.img_vida, self.poderes_sheet, self.moldura_sheet,
                       self.velocidade_pulo)
        self.cacto = Obstaculo(self.velocidade, 800, 350, self.cacto_sheet, 32, 96, self.aceleracao)
        self.mapa = Background_controller(self.layers, self.velocidade, self.aceleracao)
        self.moeda = Moeda(self.velocidade, 1000, 220, self.moeda_sheet, 48, 48, self.aceleracao)
        self.mini_moeda = Moeda(0, 970, 25, self.mini_moeda_sheet, 32, 32, 0)
        # passaro = Obstaculo(velocidade + 2, 800, --range(200,350), 96,96, aceleracao)

        self.font = pygame.font.Font("imagens/fonte/PressStart2P-vav7.ttf", 30)
        # font_lost = pygame.font.Font('freesansbold.ttf', 60)
        # pontuacao = Pontuacao()
        self.branco = (255, 255, 255)
        self.preto = (0, 0, 0)
        # FPS
        self.clock = pygame.time.Clock()
        self.fps = 60

        self.allObjects = [self.dino, self.cacto, self.moeda]

        self.moedaSound = pygame.mixer.Sound('sons/moeda.mp3')
        self.gameOverSound = pygame.mixer.Sound('sons/game_over.wav')
        self.moedaSound.set_volume(0.1)
        self.danoSound = pygame.mixer.Sound('sons/export.wav')
        self.danoSound.set_volume(0.5)