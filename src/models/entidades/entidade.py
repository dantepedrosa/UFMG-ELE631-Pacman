from abc import ABC, abstractmethod

class Entidade(ABC):
    # Valores default: caracter '?' e cor branca
    def __init__(self, x, y, caracter='?', cor='#FFFFFF'):
        self._x = x
        self._y = y
        self.caracter = caracter
        self.cor = cor

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def obter_posicao(self):
        return self._x, self._y

    def set_posicao(self, x, y):
        self._x = x
        self._y = y

    def desenhar(self):
        return self.caracter

    def colidir_com(self, outra):
        return self._x == outra.get_x() and self._y == outra.get_y()