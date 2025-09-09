from typing import List, Optional
from cliente import Cliente

class CadastroClientes:
    """
    Classe responsável pelo gerenciamento de clientes.
    
    Esta classe implementa as operações CRUD (Create, Read, Update, Delete)
    para o sistema de cadastro de clientes.
    """
    
    def __init__(self):
        """
        Inicializa o sistema de cadastro com uma lista vazia de clientes.
        """
        self._clientes: List[Cliente] = []
    
    def adicionar_cliente(self, cliente: Cliente) -> bool:
        """
        Adiciona um novo cliente ao sistema.
        
        Args:
            cliente (Cliente): Objeto cliente a ser adicionado
            
        Returns:
            bool: True se o cliente foi adicionado com sucesso, False se CPF já existe
        """
        # Verifica se já existe um cliente com o mesmo CPF
        if self.buscar_cliente_por_cpf(cliente.cpf):
            return False
        
        self._clientes.append(cliente)
        return True
    
    def listar_clientes(self) -> List[Cliente]:
        """
        Retorna a lista de todos os clientes cadastrados.
        
        Returns:
            List[Cliente]: Lista com todos os clientes
        """
        return self._clientes.copy()
    
    def buscar_cliente_por_cpf(self, cpf: str) -> Optional[Cliente]:
        """
        Busca um cliente pelo CPF.
        
        Args:
            cpf (str): CPF do cliente a ser buscado
            
        Returns:
            Optional[Cliente]: Cliente encontrado ou None se não existir
        """
        for cliente in self._clientes:
            if cliente.cpf == cpf:
                return cliente
        return None
    
    def remover_cliente(self, cpf: str) -> bool:
        """
        Remove um cliente do sistema pelo CPF.
        
        Args:
            cpf (str): CPF do cliente a ser removido
            
        Returns:
            bool: True se o cliente foi removido, False se não foi encontrado
        """
        cliente = self.buscar_cliente_por_cpf(cpf)
        if cliente:
            self._clientes.remove(cliente)
            return True
        return False
    
    def total_clientes(self) -> int:
        """
        Retorna o número total de clientes cadastrados.
        
        Returns:
            int: Número total de clientes
        """
        return len(self._clientes)
