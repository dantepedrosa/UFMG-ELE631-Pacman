from abc import abstractmethod
from .entidade import Entidade

class Item(Entidade):

    def __init__(self, x, y, **kwargs):
        # Repassa x, y e quaisquer argumentos visuais (caracter, cor) para a Entidade
        super().__init__(x, y, **kwargs)

    @abstractmethod
    def coletar(self, pacman):
        pass

    def mover(self, *args, **kwargs):
        return False