from .pellet import Pellet

class PowerPellet(Pellet):
    def __init__(self, x, y, valor=50, duracao=20):
        super().__init__(x, y, valor)
        self.simbolo = '*'
        self.duracao = duracao

    def coletar(self, pacman):
        super().coletar(pacman)
        pacman.ativar_furia(self.duracao)
        return self.valor