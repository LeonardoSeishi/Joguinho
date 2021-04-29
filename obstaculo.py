from objeto import Objeto

class Obstaculo(Objeto):
    def __init__(self, velocidade, x, y, imagem, largura, altura):
        super().__init__(imagem, x, y, largura, altura, velocidade)

