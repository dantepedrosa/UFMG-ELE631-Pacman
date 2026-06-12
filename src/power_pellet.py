from pellet import Pellet


class PowerPellet(Pellet):
    def __init__(self, x=0, y=0, valor=50, duracao=10):
        super().__init__(x, y, valor)
        self.simbolo = 'o'
        self.duracao = duracao

    def ativar_poder(self):
        return self.duracao
