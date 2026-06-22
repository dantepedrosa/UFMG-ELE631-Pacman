from abc import abstractmethod
from .entidade import Entidade

class Item(Entidade):
    @abstractmethod
    def coletar(self, pacman):
        pass

    def mover(self, *args, **kwargs):
        return False