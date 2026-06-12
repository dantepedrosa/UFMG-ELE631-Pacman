from tabuleiro import Tabuleiro
from pacman import Pacman
from fantasma import Fantasma


class Jogo:
    def __init__(self, jogador, fase=1, mapa_vazio=True):
        self.jogador = jogador
        self.fase = fase
        self.tabuleiro = Tabuleiro()
        self.pacman = Pacman(1, 1)
        self.fantasmas = []
        self.ghost_speed = self._ghost_speed_for_phase(fase)
        self.tabuleiro.inicializar(vazio=mapa_vazio)
        self._carregar_fantasmas()
        self.running = False
        self.tick = 0
        self.status_msg = ''

    def _ghost_speed_for_phase(self, fase):
        base_speed = 0.28
        velocidade = max(0.10, base_speed - (fase - 1) * 0.02)
        return velocidade

    def _carregar_fantasmas(self):
        mapa = self.tabuleiro.carregar_mapa()
        for y, linha in enumerate(mapa):
            for x, valor in enumerate(linha):
                if valor == 'G':
                    self.fantasmas.append(Fantasma(x, y))
                    self.tabuleiro.set_elemento(x, y, ' ')

    def iniciar(self):
        self.running = True
        self.tick = 0
        self._atualizar_status()
        return self.renderizar_jogo(fancy=True)

    def mover_pacman(self, direcao):
        if not self.pacman.mover(direcao, self.tabuleiro):
            return False

        item = self.tabuleiro.coletar_item(self.pacman.get_x(), self.pacman.get_y())
        self.pacman.coletar(item)
        return True

    def renderizar_jogo(self, fancy=False):
        mapa = self.tabuleiro.obter_mapa_copiado()
        px, py = self.pacman.obter_posicao()
        if 0 <= py < len(mapa) and 0 <= px < len(mapa[py]):
            mapa[py][px] = 'P'

        for fantasma in self.fantasmas:
            gx, gy = fantasma.obter_posicao()
            if 0 <= gy < len(mapa) and 0 <= gx < len(mapa[gy]):
                mapa[gy][gx] = 'G'

        return self.tabuleiro.renderizar(fancy=fancy, mapa=mapa)

    def update(self):
        if not self.running:
            return self.renderizar_jogo(), self.status()

        self.tick += 1
        for fantasma in self.fantasmas:
            fantasma.mover(self.tabuleiro, self.pacman)

        self._verificar_colisoes()
        self._atualizar_status()
        return self.renderizar_jogo(fancy=True), self.status()

    def _verificar_colisoes(self):
        for fantasma in self.fantasmas:
            if fantasma.colidir_com(self.pacman):
                if self.pacman.modo_furia:
                    fantasma.set_posicao(13, 11)
                    self.pacman.pontos += 200
                else:
                    self.pacman.perder_vida()
                    if not self.pacman.esta_vivo():
                        self.stop()
                    self.pacman.set_posicao(1, 1)
                    break

    def _atualizar_status(self):
        self.pacman.diminuir_furia()
        self.status_msg = (
            f'> STATUS: Jogador {self.jogador} | Fase {self.fase} | '
            f'Vidas {self.pacman.vidas} | Pontos {self.pacman.pontos} | '
            f'Fantasma a cada {self.ghost_speed:.2f}s'
        )
        if self.pacman.modo_furia:
            self.status_msg += f' | Fúria {self.pacman.duracao_furia}'

    def stop(self):
        self.running = False

    def status(self):
        return self.status_msg or (
            f'> STATUS: Jogador {self.jogador} | Fase {self.fase} | '
            f'Vidas {self.pacman.vidas} | Pontos {self.pacman.pontos}'
        )
