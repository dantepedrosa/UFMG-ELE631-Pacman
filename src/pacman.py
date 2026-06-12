from tabuleiro import Tabuleiro
from entidade import Entidade


class Pacman(Entidade):
    DIRECOES = {
        'UP': (0, -1),
        'DOWN': (0, 1),
        'LEFT': (-1, 0),
        'RIGHT': (1, 0),
    }

    def __init__(self, x=1, y=1, vidas=3, pontos=0):
        super().__init__(x, y, 'P')
        self.vidas = vidas
        self.pontos = pontos
        self.modo_furia = False
        self.duracao_furia = 0

    def mover(self, direcao, tabuleiro: Tabuleiro):
        if direcao not in self.DIRECOES:
            return False

        dx, dy = self.DIRECOES[direcao]
        novo_x = self._x + dx
        novo_y = self._y + dy

        if tabuleiro.eh_valido(novo_x, novo_y):
            self.set_posicao(novo_x, novo_y)
            return True

        return False

    def coletar(self, item):
        if item == '.':
            self.pontos += 10
        elif item == 'o':
            self.pontos += 50
            self.ativar_furia(20)
        return self.pontos

    def ativar_furia(self, duracao=20):
        self.modo_furia = True
        self.duracao_furia = duracao

    def diminuir_furia(self):
        if self.modo_furia:
            self.duracao_furia -= 1
            if self.duracao_furia <= 0:
                self.modo_furia = False
                self.duracao_furia = 0

    def perder_vida(self):
        self.vidas = max(0, self.vidas - 1)

    def esta_vivo(self):
        return self.vidas > 0
