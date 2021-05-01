from objeto import Objeto

class Obstaculo(Objeto):
    def __init__(self, velocidade, x, y, imagem, largura, altura, aceleracao):
        super().__init__(velocidade, x, y, imagem, largura, altura, aceleracao)

    '''def desenha(self,screen):
        screen.blit(self.imagem, (self.cordenadas[0], self.cordenadas[1]))'''

    '''def atualizar(self):
        self.objRect = pygame.Rect(self.cordenadas[0], self.cordenadas[1], self.largura, self.altura)
        self.cordenadas[0] += self.velocidade
        if self.cordenadas[0] < -100:
            self.cordenadas[0] = 1250'''
