# 1ª Atividade Parcial do Projeto 2 - Jogo PAC MAN

**Disciplina**: Análise, Projeto e Programação Orientada a Objetos  
**Prof(a)**: Luiza Bernardes Real  
**Grupo**: PAC MAN  
**Turma**: ______________________

## Integrantes do Grupo
- João Marcos Claro Porcino
- Arthur Samuel Ferreira Andrade
- Dante Junqueira Pedrosa
- Paulo Henrique Soares Gomes

---

## 1. Tema do Projeto
O tema do Projeto 2 é o **Jogo Arcade PAC MAN**, um jogo em Python que simula o labirinto, a coleta de pellets e a perseguição dos fantasmas, aplicando princípios de orientação a objeto.

## 2. Conceitos de POO Aplicados
- **a) Classes**: Usaremos classes para representar os principais elementos do jogo, como `Entidade`, `Pacman`, `Fantasma`, `Pellet`, `PowerPellet`, `Tabuleiro` e `Jogo`. Cada classe encapsula atributos e comportamentos específicos.
- **b) Herança**: A herança aparecerá na especialização das entidades. `Pacman`, `Fantasma`, `Pellet` e `PowerPellet` herdarão de `Entidade`, reaproveitando propriedades de posição e métodos básicos.
- **c) Polimorfismo**: O polimorfismo ocorrerá no método `mover()`: `Pacman` move-se com base na entrada do jogador, `Fantasma` move-se com IA/randomização e `Pellet`/`PowerPellet` podem ter comportamento passivo ou efeitos próprios ao serem coletados.
- **d) Classes Abstratas**: A classe `Entidade` atuará como abstrata, definindo a estrutura de `mover()`, `desenhar()` e atributos de posição que não devem ser instanciados diretamente.

## 3. Fluxograma Simples

```mermaid
    ---
config:
layout: dagre
---
flowchart TB
Start(["Iniciar Jogo"]) --> LoadGame["Carregar Configurações"]
LoadGame --> InitVars["Inicializar:
Vidas = 3
Score = 0
Nível = 1"]
InitVars --> RenderMap["Renderizar Mapa"]
GameLoop{"Jogo Ativo?"} -- Sim --> InputCheck["Verificar Input
do Jogador"]
InputCheck --> MovePacman["Mover Pacman"]
MovePacman --> CollectPellets["Coletar Pellets?"]
CollectPellets -- Sim --> AddScore["Aumentar Score"]
CollectPellets -- Não --> CheckPower{"Coletou
PowerUp?"}
AddScore --> CheckPower
CheckPower -- Sim --> ActivatePower["Ativar Modo Invencível
"]
CheckPower -- Não --> MoveGhosts["Mover Fantasmas"]
ActivatePower --> MoveGhosts
MoveGhosts --> CollisionCheck{"Pacman Colidiu
com Fantasma?"}
CollisionCheck -- Invencível --> EatGhost["Comer Fantasma
Score += 200
Respawnar Fantasma"]
CollisionCheck -- Normal --> LoseLife["Perder Vida
Vidas -= 1"]
LoseLife --> CheckVidas{"Vidas > 0?"}
CheckVidas -- Sim --> ResetPos["Resetar Posições
Pacman e Fantasmas"]
CheckVidas -- Não --> GameOver["GAME OVER"]
ResetPos --> CheckLevel{"Todos os
Pellets
Coletados?"}
CollisionCheck -- Nenhuma --> CheckLevel
CheckLevel -- Sim --> NextLevel["Próximo Nível
Nível += 1
Aumentar Velocidade Jogo"]
CheckLevel -- Não --> GameLoop
NextLevel --> RenderMap
RenderMap --> GameLoop
EatGhost --> CheckLevel
GameOver --> n1["Renderizar Lista de Scores"]
n2@{ label: "Receber Nome Jogador" } --> SaveScore["Salvar Score em Arquivo"]
n1 --> n2
SaveScore --> End(["Fim do Jogo"])

n1@{ shape: rect}
n2@{ shape: rect}
Start:::startEnd
LoadGame:::process
InitVars:::process
RenderMap:::process
GameLoop:::decision
InputCheck:::gameLogic
MovePacman:::process
CollectPellets:::decision
AddScore:::scoring
CheckPower:::decision
ActivatePower:::gameLogic
MoveGhosts:::process
CollisionCheck:::decision
EatGhost:::scoring
LoseLife:::scoring
CheckVidas:::decision
ResetPos:::process
GameOver:::endGame
CheckLevel:::decision
End:::startEnd
n1:::process
n2:::process
SaveScore:::scoring
classDef startEnd fill:#f0fdf4,stroke:#4ade80
classDef process fill:#eef2ff,stroke:#818cf8
classDef decision fill:#fff7ed,stroke:#fb923c
classDef gameLogic fill:#f5f3ff,stroke:#a78bfa
classDef scoring fill:#fdf4ff,stroke:#e879f9
classDef endGame fill:#fef2f2,stroke:#f87171
```

## 4. Diagrama UML de Classes

```mermaid
classDiagram
    class Entidade {
        -x: int
        -y: int
        +get_x(): int
        +get_y(): int
        +set_posicao(x: int, y: int): void
        +mover(): void
        +desenhar(): void
    }

    class Pacman {
        -vidas: int
        -pontuacao: int
        +mover(): void
        +coletar(item: string): void
    }

    class Fantasma {
        -cor: string
        -estado: string
        +mover(): void
        +perseguir(pacman: Pacman): void
    }

    class Pellet {
        -valor: int
        +mover(): void
    }

    class PowerPellet {
        -duracao: int
        +mover(): void
        +ativar_poder(): void
    }

    class Tabuleiro {
        -largura: int
        -altura: int
        -mapa: list
        +desenhar(): void
        +carregar_mapa(): void
    }

    class Jogo {
        -estado: string
        +iniciar(): void
        +atualizar(): void
        +processar_entrada(): void
    }

    class ScoreManager {
        -scores: list
        +carregar_scores(): void
        +salvar_score(nome: string, pontos: int): void
    }

    Entidade <|-- Pacman
    Entidade <|-- Fantasma
    Entidade <|-- Pellet
    Entidade <|-- PowerPellet
    Jogo --> Tabuleiro
    Jogo --> Pacman
    Jogo --> Fantasma
    Jogo --> ScoreManager
    Jogo --> Pellet
    Jogo --> PowerPellet
```

## 5. Banco de Dados

**Formato escolhido**: Arquivo CSV, por ser simples de ler/escrever e compatível com estruturas nativas de Python.

**Código de Leitura, Operação e Gravação (`salvar_score.py`)**:
```python
import csv

ARQUIVO_BD = 'scores.csv'


def ler_scores():
    with open(ARQUIVO_BD, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return [row for row in reader]


def salvar_scores(scores):
    fieldnames = ['nome', 'pontos', 'data']
    with open(ARQUIVO_BD, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(scores)


def registrar_score(nome, pontos):
    dados = ler_scores()
    novo_score = {
        'nome': nome,
        'pontos': pontos,
        'data': '2026-06-02'
    }
    dados.append(novo_score)
    salvar_scores(dados)
    print(f'Score registrado para {nome} com {pontos} pontos.')
    return dados


if __name__ == '__main__':
    registrar_score('Pacman', 1250)
```

**Base de dados original (`scores.csv`)**:
```csv
nome,pontos,data,nivel
Alice,980,2026-05-20,10
```

**Resultado após leitura, operação e gravação**:
```text
Score registrado para Pacman com 1250 pontos.
```

**Base de dados atualizada (`scores.csv`)**:
```csv
nome,pontos,data,nivel
Alice,980,2026-05-20,10
Pacman,1250,2026-06-02,2
```

## 6. Interface Gráfica
O grupo **não** utilizará interface gráfica (GUI). O jogo será executado no **terminal**, exibindo o estado do labirinto e as ações do jogador via texto.

## 7. Divisão das Implementações
As tarefas foram subdivididas entre os integrantes da seguinte forma:

- **João Marcos Claro Porcino**: Modelagem das classes `Entidade`, `Pacman`, `Fantasma`, `Pellet` e `PowerPellet` e implementação dos comportamentos de entidade.
- **Arthur Samuel Ferreira Andrade**: Modelagem de `Tabuleiro`, `Jogo` e lógica de movimentação, colisões e regras de pontuação.
- **Dante Junqueira Pedrosa**: Persistência em JSON, leitura/escrita de scores, I/O de arquivos e relatório de resultados.
- **Paulo Henrique Soares Gomes**: Interface de terminal, entrada do jogador, controle de fluxo do jogo e integração geral do código.