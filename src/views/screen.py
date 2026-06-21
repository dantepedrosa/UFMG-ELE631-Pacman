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
            vitoria = row.get('vitoria', False)
            status_v = " (VENCEU!)" if vitoria else ""
            self.score_listbox.insert(
                tk.END,
                f'{nome:<12} {pontos:>5} pts   {data}   Nível {nivel}{status_v}',
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
            height=31,
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

        self.controls_label = tk.Label(
            footer,
            text='Use setas ou WASD para mover',
            font=('Consolas', 10),
            fg=TEXT_COLOR,
            bg=PANEL_COLOR,
        )
        self.controls_label.pack(side='left')

        self.master.bind_all('<Key>', self._on_key_press)

    def _on_key_press(self, event):
        if getattr(self, 'input_paused', False) or not self.game:
            return

        key = event.keysym.upper()

        if getattr(self, 'esperando_proximo_nivel', False):
            if key == 'RETURN':
                self.proximo_nivel()
            elif key == 'ESCAPE':
                self.exit_game()
            return

        if not self.game.running:
            return
        direcoes = {
            'UP': 'UP',
            'DOWN': 'DOWN',
            'LEFT': 'LEFT',
            'RIGHT': 'RIGHT',
            'W': 'UP',
            'S': 'DOWN',
            'A': 'LEFT',
            'D': 'RIGHT',
        }
        direcao = direcoes.get(key)
        if not direcao:
            return

        vidas_antes = self.game.pacman.vidas
        self.game.mover_pacman(direcao)
        mapa_text = self.game.renderizar_jogo(fancy=True)
        status_text = self.game.status()
        self._render_and_check_status(mapa_text, status_text, vidas_antes)

        if not self.game.running:
            self.stop_loop()

    def update_map(self, mapa_text):
        self.map_area.config(state='normal')
        self.map_area.delete('1.0', tk.END)
        self.map_area.insert('1.0', mapa_text)
        self.map_area.config(state='disabled')

    def _render_and_check_status(self, mapa_text, status_text, vidas_antes):
        self.update_map(mapa_text)
        self.set_status(status_text)
        
        vidas_depois = self.game.pacman.vidas
        if vidas_depois < vidas_antes:
            if vidas_depois > 0:
                self.set_status(status_text + f"  [!] VOCÊ FOI PEGO! Retornando ao início...")
                return 2000
            else:
                self.set_status(status_text + f"  [!] GAME OVER! Pontuação: {self.game.pacman.pontos}")
                self.frame.after(3000, self.exit_game)
                return -1

        if getattr(self.game, 'vitoria', False):
            if not getattr(self, 'esperando_proximo_nivel', False):
                self.esperando_proximo_nivel = True
                self.show_victory_screen()
            return -1

        return 0

    def show_victory_screen(self):
        text = "\n\n\n\n\n\n"
        text += "       __   __ ___  _  _  ___  ___  _  _  _\n"
        text += "       \\ \\ / /| __|| \\| |/ __|| __|| || || |\n"
        text += "        \\ V / | _| | .` || (__ | _| | || ||_|\n"
        text += "         \\_/  |___||_|\\_| \\___||___| \\___/(_)\n"
        text += "\n\n"
        text += f"            PONTUAÇÃO ATUAL: {self.game.pacman.pontos}\n"
        text += f"            FASE CONCLUÍDA: {self.game.fase}\n"
        text += "\n\n"
        text += "         > PRESSIONE [ENTER] PARA PRÓXIMO NÍVEL\n"
        text += "         > PRESSIONE [ESC] PARA VOLTAR AO MENU\n"
        
        self.map_area.config(state='normal')
        self.map_area.delete('1.0', tk.END)
        self.map_area.insert('1.0', text)
        self.map_area.config(state='disabled')
        self.set_status(f"> STATUS: Aguardando jogador decidir próximo passo...")

    def proximo_nivel(self):
        self.stop_loop()
        
        # Salva o progresso atual
        if self.game:
            from src.database.manager_score import ManagerScore
            try:
                ms = ManagerScore()
                ms.adicionar_score(
                    nome=self.game.jogador,
                    pontos=self.game.pacman.pontos,
                    nivel=self.game.fase,
                    vitoria=True
                )
            except Exception as e:
                print(f"Erro ao salvar score: {e}")
        
        pontos_atuais = self.game.pacman.pontos
        vidas_atuais = self.game.pacman.vidas
        fase_nova = self.game.fase + 1
        nome = self.game.jogador
        
        from src.models.entidades.jogo import Jogo
        novo_jogo = Jogo(jogador=nome, fase=fase_nova, mapa_vazio=False)
        novo_jogo.pacman.pontos = pontos_atuais
        novo_jogo.pacman.vidas = vidas_atuais
        
        self.esperando_proximo_nivel = False
        self.game = novo_jogo
        self.game.running = True
        self.input_paused = False
        self.update_map(self.game.renderizar_jogo(fancy=True))
        self.set_status(self.game.status())
        self._run_step()

    def set_status(self, text):
        self.status_label.config(text=text)

    def start_loop(self, game):
        self.game = game
        self._run_step()

    def _run_step(self):
        if not self.game or not self.game.running:
            return

        vidas_antes = self.game.pacman.vidas
        mapa_text, status_text = self.game.update()
        delay = self._render_and_check_status(mapa_text, status_text, vidas_antes)
        
        if self.game and self.game.running and delay != -1:
            if delay > 0:
                self.input_paused = True
                self.loop_id = self.frame.after(delay, self._resume_and_run)
            else:
                self.loop_id = self.frame.after(int(self.game.ghost_speed * 1000), self._run_step)

    def _resume_and_run(self):
        self.input_paused = False
        self._run_step()

    def stop_loop(self):
        if self.loop_id is not None:
            self.frame.after_cancel(self.loop_id)
            self.loop_id = None

    def exit_game(self):
        self.stop_loop()
        if self.game:
            self.game.stop()
        self.on_exit()
