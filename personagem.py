from abc import abstractmethod
from entidade import Entidade

class Personagem(Entidade):
    # Classe abstrata para entidades que possuem capacidade de movimentação
    
    @abstractmethod
    def mover(self, *args, **kwargs):
        pass