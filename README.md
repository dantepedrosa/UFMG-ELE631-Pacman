# Projeto 2 - Jogo PAC-MAN 👾

**Disciplina**: Análise, Projeto e Programação Orientada a Objetos  
**Prof(a)**: Luiza Bernardes Real  
**Grupo**: PAC MAN  

## 👥 Integrantes do Grupo
- João Marcos Claro Porcino
- Arthur Samuel Ferreira Andrade
- Dante Junqueira Pedrosa
- Paulo Henrique Soares Gomes

---

## 🎮 1. Tema do Projeto
O tema do projeto é o clássico **Jogo Arcade PAC MAN**, recriado inteiramente em Python para ser jogado via terminal. O projeto aplica de maneira aprofundada os princípios da Programação Orientada a Objetos (POO), simulando todo o ambiente do labirinto, mecânicas de pontuação, consumo de itens (pellets) e os diferentes comportamentos de inteligência artificial na perseguição por fantasmas.

## 🏗️ 2. Arquitetura e Conceitos de POO Aplicados
O projeto passou por um processo iterativo de melhoria contínua e utiliza recursos fundamentais de POO:

- **Classes e Abstração**: Criação de classes abstratas como `Entidade`, `Personagem` e `Item` para padronizar e isolar comportamentos genéricos.
- **Herança**: As classes `Pacman` e `Fantasma` herdam de `Personagem`. Da mesma forma, os diferentes tipos de fantasmas (`Blinky`, `Pinky`, `Inky`, `Clyde`) são extensões de `Fantasma`, e os itens do jogo (`Pellet`, `PowerPellet`, `Fruta`) herdam de `Item`.
- **Polimorfismo**: Os métodos principais como `mover()` e `coletar()` respondem de maneira distinta de acordo com a instância sendo manipulada.
- **Padrões de Projeto (Strategy)**: Implementação da interface `IComportamentoMovimento` para delegar estratégias distintas de movimentação aos fantasmas (como *Chase*, *Scatter*, *Frightened* e *Retorno*), separando suas lógicas ativas de suas propriedades base.
- **Encapsulamento**: Separação clara de lógica de negócio e infraestrutura (Ex: `ManagerScore` lida exclusivamente com as regras de pontuações e ranking, enquanto o `DatabaseManager` apenas cuida das leituras e escritas no disco).

## 💾 3. Persistência de Dados
O registro e carregamento dos Rankings (*Top Scores*) foram implementados através da união interligada das classes `ManagerScore` e `DatabaseManager`:
- O armazenamento migrou na segunda etapa para o formato **JSON** (no arquivo `scores.json`), por sua facilidade de hierarquização e excelente integração com dicionários no Python.
- O sistema registra o nome do jogador, pontuação total, nível atingido, se ele finalizou o jogo com vitória e a respectiva data da partida.
- O `ManagerScore` provê os métodos que ordenam as classificações (maior pontuação e nível) para as exibições no menu principal.

## 📺 4. Interface (Terminal Mode)
O jogo possui uma interface baseada em linhas de comando e *curses/text-widgets*, dividida estruturalmente entre:
1. **Menu Inicial**: Permite preenchimento do nickname, iniciar uma partida ou consultar a tabela global de Leaderboards.
2. **Ambiente de Jogo**: O labirinto é ativamente e dinamicamente renderizado usando arte em ASCII no terminal. É atualizado na lógica de "game loop", acompanhando posições das entidades, exibindo de forma interativa a contagem de pontos, status das vidas, nível e tempo restante de modo "Fúria".

## 🚀 5. Propostas de Expansão Futura
Como visão de arquitetura em longo prazo, o sistema atual deixa portas abertas para a criação de um recurso de **Save State** (salvar uma partida no meio do labirinto). Dado que a classe `DatabaseManager` já gerencia I/O de dados, seria viável escalá-la para serializar matrizes do mapa, e instâncias atuais dos objetos (X/Y) sem precisar reestruturar as fundações do projeto.

---

## 📚 6. Referências
1. SHIVANG KUMAR. *Pac-Man with OOP*. Medium, 2020. Disponível em: [https://medium.com/@shivangk1407/pac-man-with-oop-1a26ae6c3c87](https://medium.com/@shivangk1407/pac-man-with-oop-1a26ae6c3c87).
2. CODE2BITS. *Pac-Man Patterns – Ghost Movement Strategy Pattern*. DEV Community, 2020. Disponível em: [https://dev.to/code2bits/pac-man-patterns--ghost-movement-strategy-pattern-1k1a](https://dev.to/code2bits/pac-man-patterns--ghost-movement-strategy-pattern-1k1a).