"""
Sistema de Cadastro de Clientes
===============================

Este sistema implementa um cadastro de clientes utilizando:
- Programação Orientada a Objetos (POO)
- Interface gráfica com Tkinter
- Armazenamento em memória com listas

Autor: Sistema desenvolvido para atividade acadêmica
Data: 2024

Como executar:
    python main.py

Funcionalidades:
    - Cadastrar novos clientes
    - Listar todos os clientes
    - Remover clientes por CPF
    - Interface gráfica intuitiva
"""

from interface_grafica import InterfaceGrafica

def main():
    """
    Função principal que inicia o sistema.
    """
    print("Iniciando Sistema de Cadastro de Clientes...")
    print("Desenvolvido com Python e Tkinter")
    print("=" * 50)
    
    # Criar e executar a interface gráfica
    app = InterfaceGrafica()
    app.executar()
    
    print("Sistema encerrado.")

if __name__ == "__main__":
    main()
