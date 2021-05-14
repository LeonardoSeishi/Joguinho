from random import choices


class Gerador:
    def __init__(self, screen, total_entidade=9, coeficiente_geracao=1, entidades=[]):
        self.screen = screen
        self.total_entidade = total_entidade
        self.coeficiente_geracao = coeficiente_geracao
        self.entidades = []
        self.list_pesos = []
        self.timer = 0

        for i in range(len(entidades)):
            entidade, parametros, percent = entidades[i]
            self.entidades.append((entidade, parametros))
            self.list_pesos.append(percent)

    def atualizar(self, todas_entidades):
        self.timer += 1 * self.coeficiente_geracao
        if self.timer > 80 and len(todas_entidades) < self.total_entidade:
            self.timer = 0

            randomList = choices(
                self.entidades, weights=self.list_pesos, k=1)

            entidade, parametros = randomList[0]
            obj = entidade(*parametros)
            return obj
