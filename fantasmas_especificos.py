from fantasma import Fantasma
from comportamentos import ComportamentoChase, ComportamentoScatter

class Blinky(Fantasma):
    # Fantasma vermelho: Persegue ativamente o Pac-Man
    
    def __init__(self, x=13, y=11):
        super().__init__(x, y, cor='vermelho')
        self.comportamentoAtual = ComportamentoChase()

    def mover(self, tabuleiro, pacman=None):
        if pacman is not None and self.estado == 'normal' and not getattr(pacman, 'modo_furia', False):
            self.comportamentoAtual = ComportamentoChase()
        else:
            self.comportamentoAtual = ComportamentoScatter()
            
        destino = self.comportamentoAtual.calcularDestino(self, tabuleiro, pacman)
        self.ultima_posicao = (self._x, self._y)
        self.set_posicao(*destino)
        return True


class Pinky(Fantasma):
    # Fantasma rosa: Comportamento alternativo (inicialmente aleatório para cercar)
    
    def __init__(self, x=13, y=11):
        super().__init__(x, y, cor='rosa')
        self.comportamentoAtual = ComportamentoScatter()

    def mover(self, tabuleiro, pacman=None):
        destino = self.comportamentoAtual.calcularDestino(self, tabuleiro, pacman)
        self.ultima_posicao = (self._x, self._y)
        self.set_posicao(*destino)
        return True