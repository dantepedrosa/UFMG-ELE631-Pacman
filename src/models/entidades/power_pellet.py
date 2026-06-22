from .item import Item  # Alterado para derivar diretamente de Item!

class PowerPellet(Item):
    def __init__(self, x, y, valor=50, duracao=100):
        super().__init__(x, y, caracter='o', cor='#FFD700')
        self.valor = valor
        self.simbolo = '*'
        self.duracao = duracao

    def coletar(self, pacman):
        pacman.pontos += self.valor
        pacman.ativar_furia(self.duracao)
        return self.valor