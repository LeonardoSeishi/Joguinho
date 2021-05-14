import pygame
from objeto import Objeto

class Jogador(Objeto):
    def __init__(self,velocidade , x, y, imagem: list, largura, altura, aceleracao, img_vida, img_poderes: list,img_moldura: list, velocidade_pulo):
        super().__init__(velocidade, x, y, imagem, largura, altura, aceleracao)
        self.__vidas = 3
        self.__img_vida1 = img_vida
        self.__img_vida2 = img_vida
        self.__img_vida3 = img_vida
        self.__img_escudo = img_poderes[0]
        self.__img_double_jump = img_poderes[1]
        self.__moldura = img_moldura
        self.__moldura_escudo = img_moldura[1]
        self.__moldura_double_jump = img_moldura[1]
        self.__pulando = False
        self.__agachado = False
        self.__colisao = False
        self.__escudo = False
        self.__double_jump = False
        self.__num_moedas = 0
        self.__anim_dino = 0
        self.__framerate_dino = 0
        self.__anim_moldura1 = 2
        self.__framerate_moldura1 = 0
        self.__anim_moldura2 = 2
        self.__framerate_moldura2 = 0
        self.__velocidade_pulo = velocidade_pulo

    @property
    def vidas(self):
        return self.__vidas

    @property
    def pulando(self):
        return self.__pulando

    @property
    def agachado(self):
        return self.__agachado

    @property
    def colisao(self):
        return self.__colisao

    @property
    def escudo(self):
        return self.__escudo

    @property
    def double_jump(self):
        return self.__double_jump

    @property
    def num_moedas(self):
        return self.__num_moedas

    @vidas.setter
    def vidas(self, vidas):
        self.__vidas = vidas

    @pulando.setter
    def pulando(self, boolean):
        self.__pulando = boolean

    @agachado.setter
    def agachado(self, boolean):
        self.__agachado = boolean

    @colisao.setter
    def colisao(self, boolean):
        self.__colisao = boolean

    @escudo.setter
    def escudo(self, boolean):
        self.__escudo = boolean

    @double_jump.setter
    def double_jump(self, boolean):
        self.__double_jump = boolean

    @num_moedas.setter
    def num_moedas(self, valor):
        self.__num_moedas = valor

    def set_img_escudo(self, imagem):
        self.__img_escudo = imagem

    def set_double_jump(self, imagem):
        self.__img_double_jump = imagem

    def set_img_vida1(self, imagem):
        self.__img_vida1 = imagem

    def set_img_vida2(self, imagem):
        self.__img_vida2 = imagem

    def set_img_vida3(self, imagem):
        self.__img_vida3 = imagem

    def set_moldura_escudo(self, imagem):
        self.__moldura_escudo = imagem

    def set_moldura_double_jump(self, imagem):
        self.__moldura_double_jump = imagem

    def desenha(self, screen):
        self.__framerate_dino += 1
        if self.__framerate_dino == 8:
            self.__framerate_dino = 0
            self.__anim_dino = (self.__anim_dino + 1) % len(self.imagem)
        screen.blit(self.imagem[self.__anim_dino], (self.cordenadas))
        screen.blit(self.__img_vida1, (0, 0))
        screen.blit(self.__img_vida2, (52, 0))
        screen.blit(self.__img_vida3, (104, 0))
        screen.blit(self.__img_escudo,(400,1))
        screen.blit(self.__moldura_escudo,(400,1))
        screen.blit(self.__img_double_jump,(480,1))
        screen.blit(self.__moldura_double_jump,(480,1))
        
    def atualizar(self):
        self.cordenadas[1] += self.velocidade
        self.objRect = pygame.Rect(self.cordenadas[0], self.cordenadas[1], self.largura, self.altura)

        if self.__pulando:
            self.velocidade = self.velocidade + self.aceleracao

        if self.cordenadas[1] + self.altura > 440:
            self.__pulando = False
            self.velocidade = 0     
            self.cordenadas[1] = 320

        if self.__agachado:
            if self.__pulando:
                self.cordenadas[1] += 30
            else:
                self.cordenadas[1] = 364

        if not self.__escudo:
            self.__framerate_moldura1 = 0
            self.__anim_moldura1 = 2
        else:
            self.__framerate_moldura1 += 1
            self.__moldura_escudo = self.__moldura[self.__anim_moldura1]
            if self.__framerate_moldura1 == 75:   
                if self.__anim_moldura1 == 9:
                    self.__escudo = False
                    self.__moldura_escudo = self.__moldura[1]
                    self.__anim_moldura1 = 2
                self.__framerate_moldura1 = 0
                self.__anim_moldura1 += 1
        
        if not self.__double_jump:
            self.__framerate_moldura2 = 0
            self.__anim_moldura2 = 2
        else:
            self.__framerate_moldura2 += 1
            self.__moldura_double_jump = self.__moldura[self.__anim_moldura2]
            if self.__framerate_moldura2 == 60: 
                if self.__anim_moldura2 == 9:
                    self.__double_jump = False
                    self.__moldura_double_jump = self.__moldura[1]
                    self.__anim_moldura2 = 2
                self.__framerate_moldura2 = 0
                self.__anim_moldura2 += 1


    def pular(self):
        self.__pulando = True
        self.velocidade = self.__velocidade_pulo

            