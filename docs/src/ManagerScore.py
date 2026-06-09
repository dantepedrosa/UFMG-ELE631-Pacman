
from datetime import datetime
from DatabaseManager import DatabaseManager


class ManagerScore:
    """
    Gerenciador de Scores do jogo Pac-Man.
    Responsável por gerenciar, ordenar e consultar scores dos jogadores.
    """
    
    def __init__(self, db_manager=None):
        self.db = db_manager if db_manager else DatabaseManager()
        self.scores = self.db.carregar()
    
    def adicionar_score(self, nome, pontos, nivel=1):
        if not nome or pontos < 0:
            return False
        
        score_entry = {
            'nome': nome,
            'pontos': pontos,
            'nivel': nivel,
            'data': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        self.scores.append(score_entry)
        self.ordenar_scores()
        return self.db.salvar(self.scores)
    
    def obter_top_scores(self, quantidade=10):
        return self.scores[:quantidade]
    
    def obter_score_jogador(self, nome):
        return [score for score in self.scores if score['nome'].lower() == nome.lower()]
    
    def obter_melhor_score_jogador(self, nome):
        scores_jogador = self.obter_score_jogador(nome)
        return scores_jogador[0] if scores_jogador else None
    
    def ordenar_scores(self):
        self.scores.sort(key=lambda x: (-x['pontos'], -x['nivel']))
    
    def limpar_scores(self):
        self.scores = []
        return self.db.salvar(self.scores)
    
    def exibir_ranking(self, quantidade=10):
        top_scores = self.obter_top_scores(quantidade)
        
        if not top_scores:
            return "Nenhum score registrado ainda."
        
        ranking = "=" * 70 + "\n"
        ranking += f"{'POS':<5} {'JOGADOR':<20} {'PONTOS':<10} {'NÍVEL':<10} {'DATA':<15}\n"
        ranking += "-" * 70 + "\n"
        
        for idx, score in enumerate(top_scores, 1):
            ranking += f"{idx:<5} {score['nome']:<20} {score['pontos']:<10} {score['nivel']:<10} {score['data']:<15}\n"
        
        ranking += "=" * 70
        return ranking
    
    def remover_score(self, nome, pontos):
        for score in self.scores:
            if score['nome'] == nome and score['pontos'] == pontos:
                self.scores.remove(score)
                return self.db.salvar(self.scores)
        return False
    
    def obter_total_scores(self):
        return len(self.scores)
