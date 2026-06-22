from .item import Item

class Fruta(Item):
    def __init__(self, x=0, y=0, valor=100):
        super().__init__(x, y, '@')
        self.valor = valor

    def coletar(self, pacman):
        if hasattr(pacman, 'pontos'):
            pacman.pontos += self.valor
        return self.valor