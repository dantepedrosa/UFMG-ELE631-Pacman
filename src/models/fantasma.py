import random

from .entidade import Entidade
from .tabuleiro import Tabuleiro


class Fantasma(Entidade):
    def __init__(self, x=13, y=11, cor='vermelho', estado='normal'):
        super().__init__(x, y, 'G')
        self.cor = cor
        self.estado = estado
        self.start_x = x
        self.start_y = y
        self.ultima_posicao = None

    def mover(self, tabuleiro: Tabuleiro, pacman=None):
        if pacman is not None and self.estado == 'normal' and getattr(pacman, 'modo_furia', False) == False:
            return self.perseguir(pacman, tabuleiro)
        return self._mover_aleatorio(tabuleiro)

    def perseguir(self, pacman, tabuleiro: Tabuleiro):
        movimentos = self._obter_movimentos_validos(tabuleiro)
        if not movimentos:
            return False

        if len(movimentos) > 1 and self.ultima_posicao in movimentos:
            movimentos.remove(self.ultima_posicao)

        if random.random() < 0.5:
            melhor = random.choice(movimentos)
        else:
            melhor = min(
                movimentos,
                key=lambda pos: abs(pos[0] - pacman.get_x()) + abs(pos[1] - pacman.get_y()),
            )
        self.ultima_posicao = (self._x, self._y)
        self.set_posicao(*melhor)
        return True

    def _mover_aleatorio(self, tabuleiro: Tabuleiro):
        movimentos = self._obter_movimentos_validos(tabuleiro)
        if not movimentos:
            return False

        if len(movimentos) > 1 and self.ultima_posicao in movimentos:
            movimentos.remove(self.ultima_posicao)

        escolha = random.choice(movimentos)
        self.ultima_posicao = (self._x, self._y)
        self.set_posicao(*escolha)
        return True

    def _obter_movimentos_validos(self, tabuleiro: Tabuleiro):
        possiveis = []
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            novo_x = self._x + dx
            novo_y = self._y + dy
            if tabuleiro.eh_valido(novo_x, novo_y):
                possiveis.append((novo_x, novo_y))
        return possiveis
