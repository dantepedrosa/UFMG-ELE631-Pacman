from abc import abstractmethod
from entidade import Entidade

class Item(Entidade):
    # Classe abstrata base para todos os itens coletáveis do jogo
    
    @abstractmethod
    def coletar(self, pacman):
        pass