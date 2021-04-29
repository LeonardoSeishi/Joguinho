from objeto import Objeto

class Obstaculo(Objeto):
    def __init__(self, velocidade, x, y, imagem, largura, altura):
        super().__init__(velocidade, x, y, imagem, largura, altura)

    def desenha(self,screen):
        screen.blit(self.imagem, (self.cordenadas[0], self.cordenadas[1]))

    def atualizar(self):
        self.cordenadas[0] += self.velocidade
        if self.cordenadas[0] < -100:
            self.cordenadas[0] = 1250
