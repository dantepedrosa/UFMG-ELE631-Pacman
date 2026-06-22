from abc import abstractmethod
from .entidade import Entidade

class Personagem(Entidade):
    def __init__(self, x, y, simbolo, cor='#FFFFFF'):
        super().__init__(x, y, caracter=simbolo, cor=cor)
        self.start_x = x
        self.start_y = y

    @abstractmethod
    def mover(self, *args, **kwargs):
        pass