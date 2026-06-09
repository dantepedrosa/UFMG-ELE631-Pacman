from tabuleiro import Tabuleiro


class Jogo:
    def __init__(self, jogador, fase=1, mapa_vazio=True):
        self.jogador = jogador
        self.fase = fase
        self.tabuleiro = Tabuleiro()
        self.ghost_speed = self._ghost_speed_for_phase(fase)
        self.tabuleiro.inicializar(vazio=mapa_vazio)
        self.running = False
        self.tick = 0

    def _ghost_speed_for_phase(self, fase):
        base_speed = 0.28
        velocidade = max(0.10, base_speed - (fase - 1) * 0.02)
        return velocidade

    def iniciar(self):
        self.running = True
        self.tick = 0
        # retorna mapa já com render fancy para exibição
        return self.tabuleiro.renderizar(fancy=True)

    def update(self):
        if not self.running:
            return self.tabuleiro.renderizar(), self.status()

        self.tick += 1
        # Aqui o mecanismo de atualização do jogo será adicionado.
        # Por enquanto, o mapa permanece o mesmo e apenas o status muda.
        mapa = self.tabuleiro.renderizar(fancy=True)
        status = self.status() + f' | Tick: {self.tick}'
        return mapa, status

    def stop(self):
        self.running = False

    def status(self):
        return (
            f'> STATUS: Jogador {self.jogador} | Fase {self.fase} | '
            f'Fantasma a cada {self.ghost_speed:.2f}s'
        )
