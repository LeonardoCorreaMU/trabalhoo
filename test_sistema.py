"""
Testes básicos para o sistema de cadastro de clientes.

Este arquivo contém testes simples para verificar o funcionamento
das classes Cliente e CadastroClientes.
"""

from cliente import Cliente
from cadastro_clientes import CadastroClientes

def testar_cliente():
    """
    Testa a criação e representação de um cliente.
    """
    print("Testando classe Cliente...")
    
    cliente = Cliente("João Silva", "123.456.789-00", "(11) 99999-9999", "joao@email.com")
    
    print(f"Cliente criado: {cliente}")
    print(f"Representação técnica: {repr(cliente)}")
    print("✓ Teste da classe Cliente passou\n")

def testar_cadastro():
    """
    Testa as operações de cadastro de clientes.
    """
    print("Testando classe CadastroClientes...")
    
    cadastro = CadastroClientes()
    
    # Teste 1: Adicionar cliente
    cliente1 = Cliente("Maria Santos", "987.654.321-00", "(11) 88888-8888", "maria@email.com")
    resultado = cadastro.adicionar_cliente(cliente1)
    print(f"Adicionar cliente 1: {'✓' if resultado else '✗'}")
    
    # Teste 2: Adicionar cliente duplicado (deve falhar)
    cliente_duplicado = Cliente("Outro Nome", "987.654.321-00", "(11) 77777-7777", "outro@email.com")
    resultado = cadastro.adicionar_cliente(cliente_duplicado)
    print(f"Adicionar cliente duplicado (deve falhar): {'✓' if not resultado else '✗'}")
    
    # Teste 3: Listar clientes
    clientes = cadastro.listar_clientes()
    print(f"Total de clientes: {len(clientes)}")
    
    # Teste 4: Buscar cliente por CPF
    cliente_encontrado = cadastro.buscar_cliente_por_cpf("987.654.321-00")
    print(f"Buscar cliente por CPF: {'✓' if cliente_encontrado else '✗'}")
    
    # Teste 5: Remover cliente
    resultado = cadastro.remover_cliente("987.654.321-00")
    print(f"Remover cliente: {'✓' if resultado else '✗'}")
    
    # Teste 6: Verificar se foi removido
    total_final = cadastro.total_clientes()
    print(f"Total após remoção: {total_final}")
    
    print("✓ Testes da classe CadastroClientes concluídos\n")

def main():
    """
    Executa todos os testes.
    """
    print("=" * 50)
    print("EXECUTANDO TESTES DO SISTEMA")
    print("=" * 50)
    
    testar_cliente()
    testar_cadastro()
    
    print("=" * 50)
    print("TODOS OS TESTES CONCLUÍDOS")
    print("=" * 50)

if __name__ == "__main__":
    main()
