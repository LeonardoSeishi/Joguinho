from objeto import Objeto


class Moeda(Objeto):
    def __init__(self, velocidade, x, y, imagem, largura, altura):
        super().__init__(velocidade, x, y, imagem, largura, altura)
