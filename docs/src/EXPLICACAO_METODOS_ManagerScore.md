# Explicação dos Métodos - Classe ManagerScore

## 📌 Visão Geral

A classe `ManagerScore` gerencia completamente o sistema de pontuação do jogo Pac-Man, implementando funcionalidades de registro, ordenação e consulta de scores dos jogadores.

---

## 🔧 Métodos

### 1. `__init__(self, db_manager=None)`
Inicializar o gerenciador de scores com carregamento de dados anteriormente salvos na memória.
Garante estado consistente ao iniciar.

---

### 2. `adicionar_score(self, nome, pontos, nivel=1)`
Registrar novo score quando jogador termina partida. Valida entrada e salva automaticamente. Cria entrada com nome, pontos, nível e data/hora. 

---

### 3. `obter_top_scores(self, quantidade=10)`
Recuperar os melhores scores (ranking principal). Retorna fatia da lista já ordenada. Padrão: 10 melhores.

---

### 4. `obter_score_jogador(self, nome)`
Buscar todos os scores de um jogador específico. Retorna lista com todos os scores do jogador.

---

### 5. `obter_melhor_score_jogador(self, nome)`
Retornar apenas o melhor score de um jogador. Consulta específica. Mostra recorde pessoal.


---

### 6. `ordenar_scores(self)`
Manter scores em ordem decrescente por pontos e nível. Garante rankings corretos. Critério: pontos (primário), nível (secundário).

---

### 7. `limpar_scores(self)`
Remover todos os scores do sistema. Reset para testes, desenvolvimento e novas temporadas. Limpa memória e persiste mudança.

---

### 8. `exibir_ranking(self, quantidade=10)`
Formatar e retornar ranking em string legível. Interface de apresentação. Melhora experiência do usuário. Retorna string formatada com posição, nome, pontos, nível e data. A ser atualizada e adequada corretamente à interface.

---

### 9. `remover_score(self, nome, pontos)`
Deletar score específico (manutenção de dados). Remove registros duplicados ou inválidos. Persiste mudança. Busca por combinação (nome + pontos).

---

### 10. `obter_total_scores(self)`
Retornar quantidade total de scores registrados. Informação estatística para interface e monitoramento.


---

## 📊 Fluxo Principal

```
Jogo Inicia
    ↓
__init__() carrega dados da memória
    ↓
Jogador termina partida
    ↓
adicionar_score() registra novo score
    ↓
ordenar_scores() ordena automaticamente
    ↓
Dados persistidos
    ↓
exibir_ranking() mostra ao jogador
```

