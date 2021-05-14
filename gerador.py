from random import randint


class Gerador:
    def __init__(self, screen, total_entidade=9, coeficiente_geracao=1, entidades=[]):
        self.screen = screen
        self.total_entidade = total_entidade
        self.coeficiente_geracao = coeficiente_geracao
        self.entidades = entidades
        self.timer = 0

    def atualizar(self, todas_entidades):
        self.timer += 1 * self.coeficiente_geracao
        if self.timer > 80 and len(todas_entidades) < self.total_entidade:
            self.timer = 0
            index = randint(0, len(self.entidades) - 1)
            entidade, parametros = self.entidades[index]
            obj = entidade(*parametros)
            return obj
