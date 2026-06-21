from .entidade import Entidade


class Pellet(Entidade):
    def __init__(self, x=0, y=0, valor=10):
        super().__init__(x, y, '.')
        self.valor = valor

    def mover(self, *args, **kwargs):
        return False

    def coletar(self):
        return self.valor
