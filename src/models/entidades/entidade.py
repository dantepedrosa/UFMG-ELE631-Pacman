from abc import ABC, abstractmethod


class Entidade(ABC):
    def __init__(self, x=0, y=0, simbolo='?'):
        self._x = x
        self._y = y
        self.simbolo = simbolo

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def obter_posicao(self):
        return self._x, self._y

    def set_posicao(self, x, y):
        self._x = x
        self._y = y

    def mover(self, *args, **kwargs):
        raise NotImplementedError('Classes filhas devem implementar o método mover().')

    def desenhar(self):
        return self.simbolo

    def colidir_com(self, outra):
        return self._x == outra.get_x() and self._y == outra.get_y()
