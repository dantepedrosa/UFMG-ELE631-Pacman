import json
import os


class DatabaseManager:
    """
    Gerenciador de persistência em banco de dados (JSON).
    Responsável exclusivamente por operações de leitura e escrita de dados.
    """
    
    def __init__(self, arquivo_dados='scores.json'):
        """
        Inicializa o gerenciador de banco de dados.
        
        Args:
            arquivo_dados (str): Caminho do arquivo para persistência
        """
        self.arquivo_dados = arquivo_dados
    
    def carregar(self):
        """
        Carrega dados do arquivo JSON.
        
        Returns:
            list: Lista de scores ou lista vazia se arquivo não existe
        """
        if os.path.exists(self.arquivo_dados):
            try:
                with open(self.arquivo_dados, 'r', encoding='utf-8') as arquivo:
                    dados = json.load(arquivo)
                    return dados if isinstance(dados, list) else []
            except (IOError, json.JSONDecodeError) as e:
                print(f"Erro ao carregar dados: {e}")
                return []
        return []
    
    def salvar(self, dados):
        """
        Salva dados no arquivo JSON.
        
        Args:
            dados (list): Lista de scores a salvar
        
        Returns:
            bool: True se salvo com sucesso, False caso contrário
        """
        try:
            with open(self.arquivo_dados, 'w', encoding='utf-8') as arquivo:
                json.dump(dados, arquivo, ensure_ascii=False, indent=4)
            return True
        except IOError as e:
            print(f"Erro ao salvar dados: {e}")
            return False
    
    def limpar(self):
        """
        Limpa o arquivo de dados (salva lista vazia).
        
        Returns:
            bool: True se limpo com sucesso
        """
        return self.salvar([])
    
    def arquivo_existe(self):
        """
        Verifica se o arquivo de dados existe.
        
        Returns:
            bool: True se arquivo existe
        """
        return os.path.exists(self.arquivo_dados)
