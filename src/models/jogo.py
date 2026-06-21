from .tabuleiro.tabuleiro_renderizador import TabuleiroRenderizador
from .tabuleiro.tabuleiro import Tabuleiro
from .entidades.pacman import Pacman
from .entidades.fantasma import Fantasma


class Jogo:
    def __init__(self, jogador, fase=1, mapa_vazio=True):
        self.jogador = jogador
        self.fase = fase

        self.tabuleiro = Tabuleiro()
        self.pacman = Pacman(1, 1)
        self.fantasmas = []

        self.ghost_speed = self._ghost_speed_for_phase(fase)

        self.tabuleiro.inicializar(vazio=mapa_vazio)

        # Coletar item inicial
        item_inicial = self.tabuleiro.coletar_item(
            self.pacman.get_x(),
            self.pacman.get_y()
        )
        if item_inicial:
            self.pacman.coletar(item_inicial)

        self._carregar_fantasmas()

        self.running = False
        self.tick = 0
        self.status_msg = ''
        self.vitoria = False

    def _ghost_speed_for_phase(self, fase):
        base_speed = 0.28
        return max(0.10, base_speed - (fase - 1) * 0.02)

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
        self.vitoria = False
        self._atualizar_status()
        return self.renderizar_jogo(fancy=True)

    def mover_pacman(self, direcao):
        if not self.pacman.mover(direcao, self.tabuleiro):
            return False

        item = self.tabuleiro.coletar_item(
            self.pacman.get_x(),
            self.pacman.get_y()
        )
        self.pacman.coletar(item)

        self._verificar_colisoes()

        if self.running and not self.tabuleiro.tem_itens():
            self.vitoria = True
            self.stop()

        self._atualizar_status()
        return True

    def renderizar_jogo(self, fancy=False):
        mapa = self.tabuleiro.obter_mapa_copiado()

        px, py = self.pacman.obter_posicao()
        if 0 <= py < len(mapa) and 0 <= px < len(mapa[py]):
            mapa[py][px] = 'P'

        for fantasma in self.fantasmas:
            gx, gy = fantasma.obter_posicao()
            if 0 <= gy < len(mapa) and 0 <= gx < len(mapa[gy]):
                if self.pacman.modo_furia:
                    mapa[gy][gx] = 'F'
                else:
                    mapa[gy][gx] = 'G'

        return TabuleiroRenderizador.renderizar(
            self.tabuleiro,
            fancy=fancy,
            mapa=mapa
        )

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
                    fantasma.set_posicao(
                        fantasma.start_x,
                        fantasma.start_y
                    )
                    self.pacman.pontos += 200
                else:
                    self.pacman.perder_vida()

                    if not self.pacman.esta_vivo():
                        self.stop()
                    else:
                        self.pacman.set_posicao(1, 1)
                        for f in self.fantasmas:
                            f.set_posicao(f.start_x, f.start_y)

                break

    def _atualizar_status(self):
        self.pacman.diminuir_furia()

        self.status_msg = (
            f'> STATUS: Jogador {self.jogador} | Fase {self.fase} | '
            f'Vidas {self.pacman.vidas} | Pontos {self.pacman.pontos} | '
            f'Fantasma a cada {self.ghost_speed:.2f}s'
        )

        if self.pacman.modo_furia:
            segundos_restantes = self.pacman.duracao_furia * self.ghost_speed
            self.status_msg += f' | FÚRIA: {segundos_restantes:.1f}s'

    def stop(self):
        self.running = False

    def status(self):
        return self.status_msg or (
            f'> STATUS: Jogador {self.jogador} | Fase {self.fase} | '
            f'Vidas {self.pacman.vidas} | Pontos {self.pacman.pontos}'
        )