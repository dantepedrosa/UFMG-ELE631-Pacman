from .item import Item

class Pellet(Item):
    def __init__(self, x, y, valor=10):
        super().__init__(x, y, '.')
        self.valor = valor

    def coletar(self, pacman):
        pacman.pontos += self.valor
        return self.valor