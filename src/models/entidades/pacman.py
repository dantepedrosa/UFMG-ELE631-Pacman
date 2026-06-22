from .personagem import Personagem

class Pacman(Personagem):
    DIRECOES = {
        'UP': (0, -1),
        'DOWN': (0, 1),
        'LEFT': (-1, 0),
        'RIGHT': (1, 0)
    }

    def __init__(self, x, y, vidas=3, pontos=0):
        super().__init__(x, y, 'C')
        self.vidas = vidas
        self.pontos = pontos
        self.modo_furia = False
        self.duracao_furia = 0

    def mover(self, direcao, tabuleiro):
        if direcao not in self.DIRECOES:
            return False
            
        dx, dy = self.DIRECOES[direcao]
        nx, ny = self.get_x() + dx, self.get_y() + dy
        
        if tabuleiro.eh_valido(nx, ny):
            self.set_posicao(nx, ny)
            return True
        return False

    def coletar(self, item):
        # A responsabilidade agora fica por conta do método coletar() polimórfico de cada Item
        if item:
            item.coletar(self)

    def ativar_furia(self, duracao):
        self.modo_furia = True
        self.duracao_furia = duracao

    def diminuir_furia(self):
        if self.modo_furia:
            self.duracao_furia -= 1
            if self.duracao_furia <= 0:
                self.modo_furia = False

    def perder_vida(self):
        self.vidas -= 1

    def esta_vivo(self):
        return self.vidas > 0