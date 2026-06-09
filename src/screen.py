import tkinter as tk
from tkinter import messagebox

BG_COLOR = '#050505'
PANEL_COLOR = '#0e0e0e'
TEXT_COLOR = '#00ff00'
BUTTON_BG = '#1f1f1f'
BUTTON_FG = '#00ff00'
BORDER_COLOR = '#00aa00'
MONO_FONT = 'Consolas'
MONO_FONT_BOLD = ('Consolas', 'bold')


class Screen:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master, bg=BG_COLOR)

    def show(self):
        self.frame.pack(fill='both', expand=True)

    def hide(self):
        self.frame.pack_forget()


class MainMenuScreen(Screen):
    def __init__(self, master, on_start, read_scores):
        super().__init__(master)
        self.on_start = on_start
        self.read_scores = read_scores
        self.create_widgets()
        self.load_scores()

    def create_widgets(self):
        header = tk.Frame(self.frame, bg=BG_COLOR)
        header.pack(fill='x', padx=12, pady=(12, 4))

        title = tk.Label(
            header,
            text='PAC-MAN',
            font=('Consolas', 32, 'bold'),
            fg=TEXT_COLOR,
            bg=BG_COLOR,
        )
        title.pack()

        subtitle = tk.Label(
            header,
            text='TERMINAL MODE',
            font=('Consolas', 10),
            fg='#66ff66',
            bg=BG_COLOR,
        )
        subtitle.pack(pady=(0, 8))

        panel = tk.Frame(self.frame, bg=PANEL_COLOR, bd=2, relief='solid', highlightbackground=BORDER_COLOR, highlightcolor=BORDER_COLOR, highlightthickness=1)
        panel.pack(fill='both', expand=True, padx=12, pady=(0, 12))

        prompt = tk.Label(
            panel,
            text='> BEM-VINDO AO PAC-MAN',
            font=('Consolas', 11),
            fg=TEXT_COLOR,
            bg=PANEL_COLOR,
            anchor='w',
        )
        prompt.pack(fill='x', padx=12, pady=(10, 6))

        prompt2 = tk.Label(
            panel,
            text='> DIGITE SEU NOME PARA INICIAR',
            font=('Consolas', 10),
            fg='#66ff66',
            bg=PANEL_COLOR,
            anchor='w',
        )
        prompt2.pack(fill='x', padx=12, pady=(0, 10))

        name_frame = tk.Frame(panel, bg=PANEL_COLOR)
        name_frame.pack(fill='x', padx=12, pady=(0, 10))

        tk.Label(
            name_frame,
            text='USUÁRIO:',
            font=('Consolas', 10, 'bold'),
            fg=TEXT_COLOR,
            bg=PANEL_COLOR,
        ).pack(side='left')

        self.name_entry = tk.Entry(
            name_frame,
            width=28,
            font=('Consolas', 10),
            bg='#101010',
            fg=TEXT_COLOR,
            insertbackground=TEXT_COLOR,
            relief='flat',
            highlightthickness=1,
            highlightbackground='#004400',
        )
        self.name_entry.pack(side='left', padx=(10, 0), fill='x', expand=True)

        button_frame = tk.Frame(panel, bg=PANEL_COLOR)
        button_frame.pack(fill='x', padx=12, pady=(0, 12))

        self.start_button = tk.Button(
            button_frame,
            text='> INICIAR',
            command=self.on_start_click,
            bg=BUTTON_BG,
            fg=BUTTON_FG,
            font=('Consolas', 10, 'bold'),
            relief='flat',
            activebackground='#003300',
            activeforeground=BUTTON_FG,
            bd=1,
            highlightthickness=1,
            highlightbackground=BORDER_COLOR,
        )
        self.start_button.pack(side='left', fill='x', expand=True, padx=(0, 6))

        self.refresh_button = tk.Button(
            button_frame,
            text='> ATUALIZAR',
            command=self.load_scores,
            bg=BUTTON_BG,
            fg=BUTTON_FG,
            font=('Consolas', 10, 'bold'),
            relief='flat',
            activebackground='#003300',
            activeforeground=BUTTON_FG,
            bd=1,
            highlightthickness=1,
            highlightbackground=BORDER_COLOR,
        )
        self.refresh_button.pack(side='left', fill='x', expand=True)

        score_title = tk.Label(
            panel,
            text='> TOP SCORES',
            font=('Consolas', 11, 'bold'),
            fg=TEXT_COLOR,
            bg=PANEL_COLOR,
            anchor='w',
        )
        score_title.pack(fill='x', padx=12, pady=(10, 4))

        self.score_listbox = tk.Listbox(
            panel,
            width=48,
            height=8,
            font=('Consolas', 10),
            bg='#101010',
            fg=TEXT_COLOR,
            selectbackground='#003300',
            relief='flat',
            bd=1,
        )
        self.score_listbox.pack(fill='both', expand=True, padx=12, pady=(0, 10))

        self.status_label = tk.Label(
            panel,
            text='> STATUS: AGUARDANDO COMANDO',
            font=('Consolas', 10),
            fg='#66ff66',
            bg=PANEL_COLOR,
            anchor='w',
        )
        self.status_label.pack(fill='x', padx=12, pady=(0, 12))

    def load_scores(self):
        self.score_listbox.delete(0, tk.END)
        rows = self.read_scores()
        if not rows:
            self.score_listbox.insert(tk.END, 'Nenhum score registrado ainda.')
            return

        rows_sorted = sorted(rows, key=lambda row: int(row.get('pontos', '0')), reverse=True)
        for row in rows_sorted[:10]:
            nome = row.get('nome', '')
            pontos = row.get('pontos', '0')
            data = row.get('data', '')
            nivel = row.get('nivel', '')
            self.score_listbox.insert(
                tk.END,
                f'{nome:<12} {pontos:>5} pts   {data}   Nível {nivel}',
            )

    def on_start_click(self):
        player_name = self.name_entry.get().strip()
        if not player_name:
            messagebox.showwarning('Atenção', 'Por favor, insira o nome do jogador antes de iniciar.')
            return

        self.status_label.config(text=f'> STATUS: Iniciando partida para {player_name.upper()}')
        self.on_start(player_name)
    def set_status(self, value):
        self.status_label.config(text=value)


class GameScreen(Screen):
    def __init__(self, master, on_exit):
        super().__init__(master)
        self.on_exit = on_exit
        self.game = None
        self.loop_id = None
        self.create_widgets()

    def create_widgets(self):
        header = tk.Frame(self.frame, bg=BG_COLOR)
        header.pack(fill='x', padx=12, pady=(12, 4))

        title = tk.Label(
            header,
            text='PAC-MAN - JOGO',
            font=('Consolas', 24, 'bold'),
            fg=TEXT_COLOR,
            bg=BG_COLOR,
        )
        title.pack()

        self.status_label = tk.Label(
            header,
            text='> STATUS: Jogo aguardando inicialização',
            font=('Consolas', 10),
            fg='#66ff66',
            bg=BG_COLOR,
            anchor='w',
        )
        self.status_label.pack(fill='x', pady=(4, 0))

        self.map_area = tk.Text(
            self.frame,
            width=64,
            height=28,
            font=('Consolas', 10),
            bg='#101010',
            fg=TEXT_COLOR,
            insertbackground=TEXT_COLOR,
            bd=1,
            relief='flat',
        )
        self.map_area.pack(padx=12, pady=(8, 0), fill='both', expand=True)
        self.map_area.config(state='disabled')

        footer = tk.Frame(self.frame, bg=PANEL_COLOR)
        footer.pack(fill='x', padx=12, pady=(8, 12))

        self.end_button = tk.Button(
            footer,
            text='> SAIR PARA MENU',
            command=self.exit_game,
            bg=BUTTON_BG,
            fg=BUTTON_FG,
            font=('Consolas', 10, 'bold'),
            relief='flat',
            activebackground='#003300',
            activeforeground=BUTTON_FG,
            bd=1,
            highlightthickness=1,
            highlightbackground=BORDER_COLOR,
        )
        self.end_button.pack(side='right')

    def update_map(self, mapa_text):
        self.map_area.config(state='normal')
        self.map_area.delete('1.0', tk.END)
        self.map_area.insert('1.0', mapa_text)
        self.map_area.config(state='disabled')

    def set_status(self, text):
        self.status_label.config(text=text)

    def start_loop(self, game):
        self.game = game
        self._run_step()

    def _run_step(self):
        if not self.game or not self.game.running:
            return

        mapa_text, status_text = self.game.update()
        self.update_map(mapa_text)
        self.set_status(status_text)
        self.loop_id = self.frame.after(int(self.game.ghost_speed * 1000), self._run_step)

    def stop_loop(self):
        if self.loop_id is not None:
            self.frame.after_cancel(self.loop_id)
            self.loop_id = None

    def exit_game(self):
        self.stop_loop()
        if self.game:
            self.game.stop()
        self.on_exit()
