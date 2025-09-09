class Cliente:
    """
    Classe que representa um cliente do sistema.
    
    Atributos:
        nome (str): Nome completo do cliente
        cpf (str): CPF do cliente
        telefone (str): Telefone de contato
        email (str): Email do cliente
    """
    
    def __init__(self, nome: str, cpf: str, telefone: str, email: str):
        """
        Inicializa um novo cliente.
        
        Args:
            nome (str): Nome completo do cliente
            cpf (str): CPF do cliente
            telefone (str): Telefone de contato
            email (str): Email do cliente
        """
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
    
    def __str__(self) -> str:
        """
        Retorna uma representação em string do cliente.
        
        Returns:
            str: Informações formatadas do cliente
        """
        return f"Nome: {self.nome} | CPF: {self.cpf} | Telefone: {self.telefone} | Email: {self.email}"
    
    def __repr__(self) -> str:
        """
        Retorna uma representação técnica do cliente.
        
        Returns:
            str: Representação técnica do objeto
        """
        return f"Cliente(nome='{self.nome}', cpf='{self.cpf}', telefone='{self.telefone}', email='{self.email}')"
