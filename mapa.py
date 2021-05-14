from fundo import Background

class Background_controller():
    def __init__(self, layers, velocidade: float, aceleracao: float):
        self.__layers = layers
        self.__velocidade = velocidade
        self.__aceleracao = aceleracao
        for layer in range(len(self.__layers)):
            self.__layers[(len(self.__layers)-1) - layer].velocidade = self.__velocidade
            self.__layers[(len(self.__layers)-1) - layer].aceleracao = self.__aceleracao
            if layer == 0:
                self.__velocidade += 4
            elif layer < len(self.__layers):
                self.__velocidade += 1
            else:
                self.__velocidade = -1

    @property 
    def velocidade(self):
        return self.__velocidade

    @property
    def aceleracao(self):
        return self.__aceleracao

    @velocidade.setter
    def velocidade(self, V):
        self.__velocidade = V

    @aceleracao.setter
    def aceleracao(self, A):
        self.__aceleracao = A

    def add_layer(self, layer: Background):
        self.__layers.append(layer)

    def exclui_layer(self, valor):
        self.__layers.pop(valor)

    def loop(self, screen):
        for layer in self.__layers:
            layer.atualizar()
            layer.desenha(screen)


