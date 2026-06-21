class TabuleiroRenderizador:
    """Responsavel por renderizar o tabuleiro em formato texto."""

    @staticmethod
    def renderizar(tabuleiro, fancy=False, mapa=None):
        """Retorna o mapa como string formatada."""
        mapa_atual = tabuleiro.mapa if mapa is None else mapa

        if not fancy:
            return "\n".join("".join(linha) for linha in mapa_atual)

        height = len(mapa_atual)
        width = len(mapa_atual[0]) if mapa_atual else 0

        def wall_ch(y, x):
            if mapa_atual[y][x] != "#":
                return "  "

            row_len = len(mapa_atual[y])

            top = (
                y > 0
                and x < len(mapa_atual[y - 1])
                and mapa_atual[y - 1][x] in {"#", "G"}
            )
            bottom = (
                y < height - 1
                and x < len(mapa_atual[y + 1])
                and mapa_atual[y + 1][x] in {"#", "G"}
            )
            left = x > 0 and mapa_atual[y][x - 1] in {"#", "G"}
            right = x < row_len - 1 and mapa_atual[y][x + 1] in {"#", "G"}

            if top and bottom and left and right:
                return "┼ "
            if top and bottom and left:
                return "├ "
            if top and bottom and right:
                return "┤ "
            if left and right and top:
                return "┬ "
            if left and right and bottom:
                return "┴ "
            if bottom and right:
                return "┌ "
            if bottom and left:
                return "┐ "
            if top and right:
                return "└ "
            if top and left:
                return "┘ "
            if left and right:
                return "─ "
            if top and bottom:
                return "│ "

            return "┼ "

        out_lines = []

        for y, linha in enumerate(mapa_atual):
            row = []

            for x, ch in enumerate(linha):
                if ch == "#":
                    row.append(wall_ch(y, x))
                elif ch == ".":
                    row.append("· ")
                elif ch == "o":
                    row.append("● ")
                elif ch == "G":
                    row.append("▓▓")
                elif ch == "F":
                    row.append("░░")
                elif ch == "P":
                    row.append("P ")
                elif ch == " ":
                    row.append("  ")
                elif ch == "-":
                    row.append("──")
                else:
                    row.append(f"{ch} ")

            out_lines.append("".join(row))

        return "\n".join(out_lines)

    @staticmethod
    def imprimir(tabuleiro, fancy=False):
        """Imprime o tabuleiro no terminal."""
        print(TabuleiroRenderizador.renderizar(tabuleiro, fancy=fancy))