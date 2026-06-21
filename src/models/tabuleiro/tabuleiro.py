from .tabuleiro_mapa import BOARD_LAYOUT


class Tabuleiro:
    """Representa o estado do tabuleiro do jogo."""

    def __init__(self):
        self._layout = BOARD_LAYOUT
        self.LINHAS = len(self._layout)
        self.COLUNAS = len(self._layout[0]) if self._layout else 0
        self.mapa = []
        self.inicializar(vazio=True)

    def inicializar(self, vazio=False):
        """Inicializa o mapa.

        Se vazio=True, remove pellets e power pellets.
        """
        self.mapa = [list(linha) for linha in self._layout]

        if vazio:
            self._limpar_elementos_de_jogo()

    def _limpar_elementos_de_jogo(self):
        """Remove todos os itens coletáveis do mapa."""
        for y, linha in enumerate(self.mapa):
            for x, valor in enumerate(linha):
                if valor in {'.', 'o'}:
                    self.mapa[y][x] = ' '

    def carregar_mapa(self):
        """Retorna o mapa atual."""
        return self.mapa

    def obter_mapa_copiado(self):
        """Retorna uma cópia profunda do mapa."""
        return [linha.copy() for linha in self.mapa]

    def eh_valido(self, x, y):
        """Verifica se uma posição pode ser ocupada."""
        if y < 0 or y >= self.LINHAS:
            return False

        if x < 0 or x >= len(self.mapa[y]):
            return False

        return self.mapa[y][x] != '#'

    def get_elemento(self, x, y):
        """Obtém o elemento existente em uma posição."""
        if y < 0 or y >= self.LINHAS:
            return None

        if x < 0 or x >= len(self.mapa[y]):
            return None

        return self.mapa[y][x]

    def set_elemento(self, x, y, valor):
        """Altera o conteúdo de uma posição."""
        if y < 0 or y >= self.LINHAS:
            return

        if x < 0 or x >= len(self.mapa[y]):
            return

        self.mapa[y][x] = valor

    def coletar_item(self, x, y):
        """Coleta um pellet ou power pellet da posição."""
        item = self.get_elemento(x, y)

        if item in {'.', 'o'}:
            self.set_elemento(x, y, ' ')

        return item

    def tem_itens(self):
        """Retorna True se ainda existirem itens coletáveis."""
        for linha in self.mapa:
            if '.' in linha or 'o' in linha:
                return True

        return False

    def limpar_posicao(self, x, y):
        """Limpa uma posição do mapa."""
        self.set_elemento(x, y, ' ')

    def posicionar(self, x, y, simbolo):
        """Posiciona um elemento no mapa."""
        self.set_elemento(x, y, simbolo)

    def esta_vazio(self, x, y):
        """Verifica se uma posição está vazia."""
        return self.get_elemento(x, y) == ' '