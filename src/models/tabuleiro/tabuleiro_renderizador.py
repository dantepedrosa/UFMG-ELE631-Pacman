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

        out_lines = []

        for y, linha in enumerate(mapa_atual):
            row = []

            for x, ch in enumerate(linha):
                if ch == "#":
                    row.append("███")
                elif ch == ".":
                    row.append(" · ")
                elif ch == "o":
                    row.append(" ● ")
                elif ch == " ":
                    row.append("   ")
                elif ch == "-":
                    row.append("───")
                else:
                    # Para C, B, P, @, F e qualquer entidade nova:
                    row.append(f" {ch} ")

            out_lines.append("".join(row))

        return "\n".join(out_lines)

        return "\n".join(out_lines)

    @staticmethod
    def imprimir(tabuleiro, fancy=False):
        """Imprime o tabuleiro no terminal."""
        print(TabuleiroRenderizador.renderizar(tabuleiro, fancy=fancy))