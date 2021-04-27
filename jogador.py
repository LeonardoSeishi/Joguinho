class Jogador():
    def __init__(self,velocidade, x, y, imagem, largura, altura):
        super().__init__(imagem, x, y, largura, altura, velocidade = None)
        self.__pulando = False
        self.__agachado = False
        self.__gravidade = 0.25

    def atualizar(self):
        self.__posicao[1] += self.__velocidade

        if self.__velocidade<= 11.1 and self.__velocidade >= 10.9:
            self.__pulando = False     
            self.__posicao[1] = 317

        if self.__pulando:
            self.__velocidade = self.__velocidade + self.__gravidade
            
    def pular():
        self.__pulando = True
        self.__velocidade = -11


            