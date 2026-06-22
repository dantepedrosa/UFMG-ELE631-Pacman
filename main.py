import csv
import os
import sys

# Adiciona a pasta src ao path do Python para resolver os imports internos
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))
import tkinter as tk
from tkinter import messagebox

from src.models.jogo import Jogo
from src.views.screen import MainMenuScreen, GameScreen, BG_COLOR
from src.database.manager_score import ManagerScore


class MenuApp:
    def __init__(self, root):
        self.root = root
        self.root.title('PAC-MAN - Menu Inicial')
        self.root.configure(bg=BG_COLOR)
        self.root.resizable(False, False)

        self.root.geometry('1130x1080')

        self.game = None
        self.main_screen = MainMenuScreen(root, self.start_game, self.read_scores)
        self.game_screen = GameScreen(root, self.end_game)

        self.main_screen.show()

    def read_scores(self):
        try:
            ms = ManagerScore()
            return ms.obter_top_scores(10)
        except Exception:
            return []

    def start_game(self, player_name):
        self.game = Jogo(player_name, fase=1, mapa_vazio=False)
        mapa_inicial = self.game.iniciar()

        self.main_screen.hide()
        self.game_screen.show()
        self.game_screen.update_map(mapa_inicial)
        self.game_screen.set_status(self.game.status())
        self.game_screen.start_loop(self.game)

    def end_game(self):
        # Pega a referência atualizada do jogo a partir da tela (pois o nível pode ter mudado)
        current_game = self.game_screen.game if hasattr(self, 'game_screen') else self.game
        if current_game:
            try:
                ms = ManagerScore()
                ms.adicionar_score(
                    nome=current_game.jogador,
                    pontos=current_game.pacman.pontos,
                    nivel=current_game.fase,
                    vitoria=getattr(current_game, 'vitoria', False)
                )
            except Exception as e:
                print(f"Erro ao salvar score: {e}")

            if self.game:
                self.game.stop()
            self.game = None

        self.game_screen.hide()
        self.main_screen.load_scores()
        self.main_screen.show()


def main():
    root = tk.Tk()
    app = MenuApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()
