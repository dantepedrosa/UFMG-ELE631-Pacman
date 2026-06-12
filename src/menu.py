import csv
import os
import tkinter as tk
from tkinter import messagebox

from jogo import Jogo
from screen import MainMenuScreen, GameScreen, BG_COLOR

SCORES_FILE = 'scores.csv'


def read_scores(path=SCORES_FILE):
    if not os.path.exists(path):
        return []

    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)


class MenuApp:
    def __init__(self, root):
        self.root = root
        self.root.title('PAC-MAN - Menu Inicial')
        self.root.configure(bg=BG_COLOR)
        self.root.resizable(False, False)

        self.game = None
        self.main_screen = MainMenuScreen(root, self.start_game, self.read_scores)
        self.game_screen = GameScreen(root, self.end_game)

        self.main_screen.show()

    def read_scores(self):
        return read_scores()

    def start_game(self, player_name):
        self.game = Jogo(player_name, fase=1, mapa_vazio=False)
        mapa_inicial = self.game.iniciar()

        self.main_screen.hide()
        self.game_screen.show()
        self.game_screen.update_map(mapa_inicial)
        self.game_screen.set_status(self.game.status())
        self.game_screen.start_loop(self.game)

    def end_game(self):
        if self.game:
            self.game.stop()
            self.game = None

        self.game_screen.hide()
        self.main_screen.show()


def main():
    root = tk.Tk()
    app = MenuApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()
