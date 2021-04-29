from objeto import Objeto

class Obstaculo_movel(Objeto):
    def __init__(self, velocidade, x, y, imagem, largura, altura):
        super().__init__(imagem, x, y, largura, altura, velocidade)