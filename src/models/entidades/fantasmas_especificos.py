from .fantasma import Fantasma
from .comportamentos import ComportamentoChase, ComportamentoScatter

class Blinky(Fantasma):
    def __init__(self, x, y):
        super().__init__(x, y, cor='#FF0000')
        self.simbolo = 'B'
        self.comportamentoAtual = ComportamentoChase()

    def mover(self, tabuleiro, pacman=None):
        if pacman is not None and self.estado == 'normal' and not getattr(pacman, 'modo_furia', False):
            self.comportamentoAtual = ComportamentoChase()
        else:
            self.comportamentoAtual = ComportamentoScatter()
            
        destino = self.comportamentoAtual.calcularDestino(self, tabuleiro, pacman)
        self.ultima_posicao = self.obter_posicao()
        self.set_posicao(*destino)
        return True


class Pinky(Fantasma):
    def __init__(self, x, y):
        super().__init__(x, y, cor='#FFB8FF')
        self.simbolo = 'P'
        self.comportamentoAtual = ComportamentoScatter()

    def mover(self, tabuleiro, pacman=None):
        destino = self.comportamentoAtual.calcularDestino(self, tabuleiro, pacman)
        self.ultima_posicao = self.obter_posicao()
        self.set_posicao(*destino)
        return True