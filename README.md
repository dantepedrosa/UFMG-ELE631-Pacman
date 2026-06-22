# Projeto 2 - Jogo PAC-MAN 👾

**Disciplina**: Análise, Projeto e Programação Orientada a Objetos

**Prof(a)**: Luiza Bernardes Real

**Grupo**: PAC MAN

## 👥 Integrantes do Grupo

* João Marcos Claro Porcino
* Arthur Samuel Ferreira Andrade
* Dante Junqueira Pedrosa
* Paulo Henrique Soares Gomes

---

## 🎮 1. Tema do Projeto

O tema do projeto é o clássico **Jogo Arcade PAC MAN**, recriado inteiramente em Python. O projeto aplica de maneira aprofundada os princípios da Programação Orientada a Objetos (POO), simulando todo o ambiente do labirinto, mecânicas de pontuação, consumo de itens (pellets) e os diferentes comportamentos de inteligência artificial na perseguição por fantasmas.

## 🏗️ 2. Arquitetura e Conceitos de POO Aplicados

O projeto passou por um processo iterativo de melhoria contínua e utiliza recursos fundamentais de POO:

* **Classes e Abstração**: Criação de classes abstratas como `Entidade`, `Personagem` e `Item` para padronizar e isolar comportamentos genéricos.
* **Herança**: As classes `Pacman` e `Fantasma` herdam de `Personagem`. Da mesma forma, os diferentes tipos de fantasmas (`Blinky`, `Pinky`, `Inky`, `Clyde`) são extensões de `Fantasma`, e os itens do jogo (`Pellet`, `PowerPellet`, `Fruta`) herdam de `Item`.
* **Polimorfismo**: Os métodos principais como `mover()` e `coletar()` respondem de maneira distinta de acordo com a instância sendo manipulada.
* **Padrões de Projeto (Strategy)**: Implementação da interface `IComportamentoMovimento` para delegar estratégias distintas de movimentação aos fantasmas (como *Chase*, *Scatter*, *Frightened* e *Retorno*), separando suas lógicas ativas de suas propriedades base.
* **Encapsulamento**: Separação clara de lógica de negócio e infraestrutura (Ex: `ManagerScore` lida exclusivamente com as regras de pontuações e ranking, enquanto o `DatabaseManager` apenas cuida das leituras e escritas no disco).

## 💾 3. Persistência de Dados

O registro e carregamento dos Rankings (*Top Scores*) foram implementados através da união interligada das classes `ManagerScore` e `DatabaseManager`:

* O armazenamento migrou na segunda etapa para o formato **JSON** (no arquivo `scores.json`), por sua facilidade de hierarquização e excelente integração com dicionários no Python.
* O sistema registra o nome do jogador, pontuação total, nível atingido, se ele finalizou o jogo com vitória e a respectiva data da partida.
* O `ManagerScore` provê os métodos que ordenam as classificações (maior pontuação e nível) para as exibições no menu principal.

## 📺 4. Interface e Visualização

O jogo possui uma interface interativa estruturada através do módulo `Tkinter` (na camada de *views*), dividida entre:

1. **Menu Inicial**: Permite preenchimento do nickname, iniciar uma partida ou consultar a tabela global de Leaderboards.
2. **Ambiente de Jogo**: O labirinto é ativamente e dinamicamente renderizado. É atualizado na lógica de "game loop", acompanhando posições das entidades, exibindo de forma interativa a contagem de pontos, status das vidas, nível e tempo restante de modo "Fúria".

## 📁 5. Estrutura do Projeto

A organização do código segue uma arquitetura modular separando dados, visualização e regras de negócio:

* `docs/`: Documentação e entregas parciais do projeto.
* `src/models/`: Lógica central do jogo, incluindo Entidades (Pacman, Fantasmas, Itens) e Tabuleiro.
* `src/views/`: Telas e interface gráfica (`GameScreen`, `MainMenuScreen`).
* `src/database/`: Gerenciamento de persistência de dados.
* `main.py`: Arquivo principal e ponto de entrada da aplicação.
* `scores.json`: Arquivo de armazenamento das pontuações de jogadores.

## ⚙️ 6. Instalação e Requisitos

Crie um arquivo `requirements.txt` na raiz do seu projeto com o seguinte conteúdo de instrução para facilitar a configuração do ambiente:

```text
# Requirements.txt - Dependências do Projeto PAC-MAN
# 
# Nota: Este projeto usa apenas módulos built-in do Python.
# Tkinter vem pré-instalado com Python 3.
# 
# Se você estiver em um Linux e tkinter não estiver disponível:
#   Ubuntu/Debian: sudo apt-get install python3-tk
#   Fedora/RHEL: sudo yum install python3-tkinter
#   Arch: sudo pacman -S tk
#
# Após instalar tkinter, execute:
#   python3 -m venv venv
#   source venv/bin/activate  # No Windows: venv\Scripts\activate
#   pip install -r requirements.txt

```

Para rodar o jogo, navegue até a raiz do projeto e execute:

```bash
python main.py

```

## 🚀 7. Propostas de Expansão Futura

Como visão de arquitetura em longo prazo, o sistema atual deixa portas abertas para a criação de um recurso de **Save State** (salvar uma partida no meio do labirinto). Dado que a classe `DatabaseManager` já gerencia I/O de dados, seria viável escalá-la para serializar matrizes do mapa, e instâncias atuais dos objetos (X/Y) sem precisar reestruturar as fundações do projeto.

---

## 📚 8. Referências

1. SHIVANG KUMAR. *Pac-Man with OOP*. Medium, 2020. Disponível em: [https://medium.com/@shivangk1407/pac-man-with-oop-1a26ae6c3c87](https://medium.com/@shivangk1407/pac-man-with-oop-1a26ae6c3c87).
2. CODE2BITS. *Pac-Man Patterns – Ghost Movement Strategy Pattern*. DEV Community, 2020. Disponível em: [https://dev.to/code2bits/pac-man-patterns--ghost-movement-strategy-pattern-1k1a](https://dev.to/code2bits/pac-man-patterns--ghost-movement-strategy-pattern-1k1a).