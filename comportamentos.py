from abc import ABC, abstractmethod
import random

class IComportamentoMovimento(ABC):
    # Interface para o padrão Strategy de movimentação dos fantasmas
    
    @abstractmethod
    def calcularDestino(self, fantasma, tabuleiro, pacman=None):
        pass


class ComportamentoChase(IComportamentoMovimento):
    # Estratégia de perseguição direta ao Pac-Man
    
    def calcularDestino(self, fantasma, tabuleiro, pacman=None):
        if not pacman:
            return fantasma.obter_posicao()
            
        movimentos = fantasma._obter_movimentos_validos(tabuleiro)
        if not movimentos:
            return fantasma.obter_posicao()
            
        # Evita voltar imediatamente para a posição anterior
        if len(movimentos) > 1 and fantasma.ultima_posicao in movimentos:
            movimentos.remove(fantasma.ultima_posicao)
            
        melhor_movimento = min(
            movimentos,
            key=lambda pos: abs(pos[0] - pacman.get_x()) + abs(pos[1] - pacman.get_y())
        )
        return melhor_movimento


class ComportamentoScatter(IComportamentoMovimento):
    # Estratégia de movimentação aleatória (fuga ou dispersão)
    
    def calcularDestino(self, fantasma, tabuleiro, pacman=None):
        movimentos = fantasma._obter_movimentos_validos(tabuleiro)
        if not movimentos:
            return fantasma.obter_posicao()
            
        if len(movimentos) > 1 and getattr(fantasma, 'ultima_posicao', None) in movimentos:
            movimentos.remove(fantasma.ultima_posicao)
            
        return random.choice(movimentos)