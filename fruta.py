from item import Item

class Fruta(Item):
    # Representa um item bônus que concede pontuação extra ao Pac-Man
    
    def __init__(self, x=0, y=0, valor=100):
        super().__init__(x, y, 'C') # 'C' representa Cherry (Cereja)
        self.valor = valor

    def mover(self, *args, **kwargs):
        return False

    def coletar(self, pacman):
        if hasattr(pacman, 'pontos'):
            pacman.pontos += self.valor
        return self.valor