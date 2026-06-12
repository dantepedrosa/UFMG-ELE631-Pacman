class Tabuleiro:
    """Classe que gera o mapa base do Pac-Man e permite criar uma versão vazia."""

    def __init__(self):
        self._layout = self._build_original_layout()
        self.LINHAS = len(self._layout)
        self.COLUNAS = len(self._layout[0]) if self._layout else 0
        self.mapa = []
        self.inicializar(vazio=True)

    def _build_original_layout(self):
        return [
            "############################",
            "#............##............#",
            "#.####.#####.##.#####.####.#",
            "#o####.#####.##.#####.####o#",
            "#.####.#####.##.#####.####.#",
            "#..........................#",
            "#.####.##.########.##.####.#",
            "#.####.##.########.##.####.#",
            "#......##....##....##......#",
            "######.##### ## #####.######",
            "     #.##### ## #####.#     ",
            "     #.##          ##.#     ",
            "     #.## ###--### ##.#     ",
            "######.## #GGGG# ##.######",
            "       .   #GGGG#   .       ",
            "######.## ###### ##.######",
            "     #.##          ##.#     ",
            "     #.## ######## ##.#     ",
            "######.## ######## ##.######",
            "#............##............#",
            "#.####.#####.##.#####.####.#",
            "#.####.#####.##.#####.####.#",
            "#o..##.......  .......##..o#",
            "###.##.##.########.##.##.###",
            "###.##.##.########.##.##.###",
            "#......##....##....##......#",
            "#.##########.##.##########.#",
            "#.##########.##.##########.#",
            "#..........................#",
            "############################",
        ]

    def inicializar(self, vazio=False):
        """Inicializa o mapa do tabuleiro.

        Se vazio=True, a estrutura do labirinto é carregada com paredes e espaços vazios.
        Se vazio=False, os pontos e power-ups também são mantidos.
        """
        self.mapa = [list(linha) for linha in self._layout]
        if vazio:
            self._limpar_elementos_de_jogo()

    def _limpar_elementos_de_jogo(self):
        for y, linha in enumerate(self.mapa):
            for x, valor in enumerate(linha):
                if valor in {'.', 'o'}:
                    self.mapa[y][x] = ' '

    def carregar_mapa(self):
        return self.mapa

    def obter_mapa_copiado(self):
        return [linha.copy() for linha in self.mapa]

    def eh_valido(self, x, y):
        if y < 0 or y >= self.LINHAS:
            return False
        if x < 0 or x >= len(self.mapa[y]):
            return False
        return self.mapa[y][x] != '#'

    def get_elemento(self, x, y):
        if y < 0 or y >= self.LINHAS or x < 0 or x >= len(self.mapa[y]):
            return None
        return self.mapa[y][x]

    def set_elemento(self, x, y, valor):
        if y < 0 or y >= self.LINHAS:
            return
        if x < 0 or x >= len(self.mapa[y]):
            return
        self.mapa[y][x] = valor

    def coletar_item(self, x, y):
        item = self.get_elemento(x, y)
        if item in {'.', 'o'}:
            self.set_elemento(x, y, ' ')
        return item

    def renderizar(self, fancy=False, mapa=None):
        """Retorna o mapa como texto."""
        mapa_atual = self.mapa if mapa is None else mapa
        if not fancy:
            return '\n'.join(''.join(linha) for linha in mapa_atual)

        height = len(mapa_atual)
        width = len(mapa_atual[0]) if mapa_atual else 0

        def wall_ch(y, x):
            if mapa_atual[y][x] != '#':
                return '  '

            row_len = len(mapa_atual[y])
            top = y > 0 and x < len(mapa_atual[y - 1]) and mapa_atual[y - 1][x] in {'#', 'G'}
            bottom = y < height - 1 and x < len(mapa_atual[y + 1]) and mapa_atual[y + 1][x] in {'#', 'G'}
            left = x > 0 and mapa_atual[y][x - 1] in {'#', 'G'}
            right = x < row_len - 1 and mapa_atual[y][x + 1] in {'#', 'G'}

            if top and bottom and left and right:
                return '┼ '
            if top and bottom and left:
                return '├ '
            if top and bottom and right:
                return '┤ '
            if left and right and top:
                return '┬ '
            if left and right and bottom:
                return '┴ '
            if bottom and right:
                return '┌ '
            if bottom and left:
                return '┐ '
            if top and right:
                return '└ '
            if top and left:
                return '┘ '
            if left and right:
                return '─ '
            if top and bottom:
                return '│ '
            return '┼ '

        out_lines = []
        for y, linha in enumerate(mapa_atual):
            row = []
            for x, ch in enumerate(linha):
                if ch == '#':
                    row.append(wall_ch(y, x))
                elif ch == '.':
                    row.append('· ')
                elif ch == 'o':
                    row.append('● ')
                elif ch == 'G':
                    row.append('▓▓')
                elif ch == 'P':
                    row.append('P ')
                elif ch == ' ': 
                    row.append('  ')
                elif ch == '-':
                    row.append('──')
                else:
                    row.append(f'{ch} ')
            out_lines.append(''.join(row))
        return '\n'.join(out_lines)

    def imprime(self):
        print(self.renderizar())
