from objeto import Objeto

class Obstaculo(Objeto):
    def __init__(self, velocidade, x, y, imagem, largura, altura, aceleracao):
        super().__init__(velocidade, x, y, imagem, largura, altura, aceleracao)

