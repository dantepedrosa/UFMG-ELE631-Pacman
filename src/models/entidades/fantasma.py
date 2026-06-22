from .personagem import Personagem

class Fantasma(Personagem):
    def __init__(self, x, y, cor, estado='normal'):
        super().__init__(x, y, simbolo='ᗣ', cor=cor)
        self.cor = cor
        self.estado = estado
        self.ultima_posicao = None

    def _obter_movimentos_validos(self, tabuleiro):
        movimentos = []
        x, y = self.obter_posicao()
        direcoes = [(0, -1), (0, 1), (-1, 0), (1, 0)] 
        
        for dx, dy in direcoes:
            nx, ny = x + dx, y + dy
            if tabuleiro.eh_valido(nx, ny):
                movimentos.append((nx, ny))
                
        return movimentos