from .tabuleiro.tabuleiro_renderizador import TabuleiroRenderizador
from .tabuleiro.tabuleiro import Tabuleiro
from .entidades.pacman import Pacman
from .entidades.fantasmas_especificos import Blinky, Pinky
from .entidades.pellet import Pellet
from .entidades.power_pellet import PowerPellet
from .entidades.fruta import Fruta

class Jogo:
    def __init__(self, jogador, fase=1, mapa_vazio=True):
        self.jogador = jogador
        self.fase = fase

        self.tabuleiro = Tabuleiro()
        self.pacman = Pacman(1, 1)
        self.fantasmas = []

        self.ghost_speed = self._ghost_speed_for_phase(fase)

        self.tabuleiro.inicializar(vazio=mapa_vazio)

        # Atualizado: usa o novo método processador de itens
        item_inicial = self.tabuleiro.coletar_item(
            self.pacman.get_x(),
            self.pacman.get_y()
        )
        self._processar_coleta(item_inicial, self.pacman.get_x(), self.pacman.get_y())

        self._carregar_fantasmas()

        self.running = False
        self.tick = 0
        self.status_msg = ''
        self.vitoria = False

    def _processar_coleta(self, simbolo, x, y):
        """Converte o caractere do tabuleiro em um Objeto Item real."""
        if simbolo == '.':
            self.pacman.coletar(Pellet(x, y))
        elif simbolo == 'o':
            self.pacman.coletar(PowerPellet(x, y))
        elif simbolo == '@':
            self.pacman.coletar(Fruta(x, y))

    def _ghost_speed_for_phase(self, fase):
        base_speed = 0.28
        return max(0.10, base_speed - (fase - 1) * 0.02)

    def _carregar_fantasmas(self):
        mapa = self.tabuleiro.carregar_mapa()
        contador = 0

        for y, linha in enumerate(mapa):
            for x, valor in enumerate(linha):
                if valor == 'G':
                    if contador % 2 == 0:
                        self.fantasmas.append(Blinky(x, y))
                    else:
                        self.fantasmas.append(Pinky(x, y))
                    contador += 1
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

        # Atualizado: usa o novo método processador de itens
        item_str = self.tabuleiro.coletar_item(
            self.pacman.get_x(),
            self.pacman.get_y()
        )
        self._processar_coleta(item_str, self.pacman.get_x(), self.pacman.get_y())

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
            mapa[py][px] = 'C'

        for fantasma in self.fantasmas:
            gx, gy = fantasma.obter_posicao()
            if 0 <= gy < len(mapa) and 0 <= gx < len(mapa[gy]):
                if getattr(self.pacman, 'modo_furia', False):
                    mapa[gy][gx] = 'F'
                else:
                    mapa[gy][gx] = fantasma.simbolo

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
                if getattr(self.pacman, 'modo_furia', False):
                    fantasma.set_posicao(
                        getattr(fantasma, 'start_x', 1),
                        getattr(fantasma, 'start_y', 1)
                    )
                    self.pacman.pontos += 200
                else:
                    self.pacman.perder_vida()

                    if not self.pacman.esta_vivo():
                        self.stop()
                    else:
                        self.pacman.set_posicao(1, 1)
                        for f in self.fantasmas:
                            f.set_posicao(
                                getattr(f, 'start_x', 1), 
                                getattr(f, 'start_y', 1)
                            )
                break

    def _atualizar_status(self):
        self.pacman.diminuir_furia()

        self.status_msg = (
            f'> STATUS: Jogador {self.jogador} | Fase {self.fase} | '
            f'Vidas {self.pacman.vidas} | Pontos {self.pacman.pontos} | '
            f'Fantasma a cada {self.ghost_speed:.2f}s'
        )

        if getattr(self.pacman, 'modo_furia', False):
            segundos_restantes = self.pacman.duracao_furia * self.ghost_speed
            self.status_msg += f' | FÚRIA: {segundos_restantes:.1f}s'

    def stop(self):
        self.running = False

    def status(self):
        return self.status_msg or (
            f'> STATUS: Jogador {self.jogador} | Fase {self.fase} | '
            f'Vidas {self.pacman.vidas} | Pontos {self.pacman.pontos}'
        )
    
    def obter_mapa_cores(self):
        """Retorna um dicionário mapeando os caracteres do tabuleiro para suas cores."""
        # Verifica se o Pacman existe e está no modo furia
        furia_ativo = getattr(self.pacman, 'modo_furia', False)
        cor_fantasma_medo = '#0000FF'  # Azul Arcade clássico

        # Cores padrão para o Pacman e Itens do mapa
        cores = {
            'C': getattr(self.pacman, 'cor', '#FFFF00'),  # Amarelo
            '·': '#FFB8AE',  # Cor do pellet (rosa claro)
            '●': '#FFB8FF',  # Cor do power pellet
            '@': '#00FF00',  # Cor da fruta
        }
        
        # Busca dinamicamente a cor de cada fantasma instanciado
        for f in self.fantasmas:
            simbolo = getattr(f, 'simbolo', 'G')
            if furia_ativo:
                # Se estiver em modo fúria, a cor na tela vira azul
                cores[simbolo] = cor_fantasma_medo
            else:
                # Caso contrário, usa a cor padrão deles (Vermelho, Rosa, etc.)
                cores[simbolo] = getattr(f, 'cor', '#FF0000')
            
        # Mapeamento para as paredes (caracteres fancy do TabuleiroRenderizador)
        cor_parede = '#1919A6'  # Azul escuro estilo Arcade
        for char in '┼├┤┬┴┌┐└┘─│#':
            cores[char] = cor_parede
            
        return cores