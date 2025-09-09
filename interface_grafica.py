import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from cliente import Cliente
from cadastro_clientes import CadastroClientes

class InterfaceGrafica:
    """
    Classe responsável pela interface gráfica do sistema de cadastro de clientes.
    
    Utiliza a biblioteca Tkinter para criar uma interface desktop amigável
    para gerenciamento de clientes.
    """
    
    def __init__(self):
        """
        Inicializa a interface gráfica e o sistema de cadastro.
        """
        self.cadastro = CadastroClientes()
        self.root = tk.Tk()
        self.configurar_janela()
        self.criar_widgets()
    
    def configurar_janela(self):
        """
        Configura as propriedades principais da janela.
        """
        self.root.title("Sistema de Cadastro de Clientes")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # Centralizar a janela na tela
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (800 // 2)
        y = (self.root.winfo_screenheight() // 2) - (600 // 2)
        self.root.geometry(f"800x600+{x}+{y}")
    
    def criar_widgets(self):
        """
        Cria todos os widgets da interface gráfica.
        """
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Título
        titulo = ttk.Label(main_frame, text="Sistema de Cadastro de Clientes", 
                          font=("Arial", 16, "bold"))
        titulo.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Frame para entrada de dados
        self.criar_frame_entrada(main_frame)
        
        # Frame para botões
        self.criar_frame_botoes(main_frame)
        
        # Frame para listagem
        self.criar_frame_listagem(main_frame)
        
        # Frame para remoção
        self.criar_frame_remocao(main_frame)
    
    def criar_frame_entrada(self, parent):
        """
        Cria o frame com os campos de entrada de dados.
        
        Args:
            parent: Widget pai onde o frame será inserido
        """
        # Frame de entrada
        entrada_frame = ttk.LabelFrame(parent, text="Cadastrar Novo Cliente", padding="10")
        entrada_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        entrada_frame.columnconfigure(1, weight=1)
        
        # Campos de entrada
        ttk.Label(entrada_frame, text="Nome:").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.entry_nome = ttk.Entry(entrada_frame, width=40)
        self.entry_nome.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(10, 0), pady=2)
        
        ttk.Label(entrada_frame, text="CPF:").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.entry_cpf = ttk.Entry(entrada_frame, width=40)
        self.entry_cpf.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=(10, 0), pady=2)
        
        ttk.Label(entrada_frame, text="Telefone:").grid(row=2, column=0, sticky=tk.W, pady=2)
        self.entry_telefone = ttk.Entry(entrada_frame, width=40)
        self.entry_telefone.grid(row=2, column=1, sticky=(tk.W, tk.E), padx=(10, 0), pady=2)
        
        ttk.Label(entrada_frame, text="Email:").grid(row=3, column=0, sticky=tk.W, pady=2)
        self.entry_email = ttk.Entry(entrada_frame, width=40)
        self.entry_email.grid(row=3, column=1, sticky=(tk.W, tk.E), padx=(10, 0), pady=2)
    
    def criar_frame_botoes(self, parent):
        """
        Cria o frame com os botões de ação.
        
        Args:
            parent: Widget pai onde o frame será inserido
        """
        botoes_frame = ttk.Frame(parent)
        botoes_frame.grid(row=2, column=0, columnspan=2, pady=10)
        
        ttk.Button(botoes_frame, text="Cadastrar Cliente", 
                  command=self.cadastrar_cliente).pack(side=tk.LEFT, padx=5)
        ttk.Button(botoes_frame, text="Listar Clientes", 
                  command=self.listar_clientes).pack(side=tk.LEFT, padx=5)
        ttk.Button(botoes_frame, text="Limpar Campos", 
                  command=self.limpar_campos).pack(side=tk.LEFT, padx=5)
    
    def criar_frame_listagem(self, parent):
        """
        Cria o frame para exibição da lista de clientes.
        
        Args:
            parent: Widget pai onde o frame será inserido
        """
        listagem_frame = ttk.LabelFrame(parent, text="Clientes Cadastrados", padding="10")
        listagem_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        listagem_frame.columnconfigure(0, weight=1)
        listagem_frame.rowconfigure(0, weight=1)
        
        # Área de texto com scroll para listagem
        self.text_listagem = scrolledtext.ScrolledText(listagem_frame, height=10, width=70)
        self.text_listagem.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    
    def criar_frame_remocao(self, parent):
        """
        Cria o frame para remoção de clientes.
        
        Args:
            parent: Widget pai onde o frame será inserido
        """
        remocao_frame = ttk.LabelFrame(parent, text="Remover Cliente", padding="10")
        remocao_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E))
        remocao_frame.columnconfigure(1, weight=1)
        
        ttk.Label(remocao_frame, text="CPF para remoção:").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.entry_cpf_remocao = ttk.Entry(remocao_frame, width=30)
        self.entry_cpf_remocao.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(10, 0), pady=2)
        
        ttk.Button(remocao_frame, text="Remover Cliente", 
                  command=self.remover_cliente).grid(row=0, column=2, padx=(10, 0))
    
    def cadastrar_cliente(self):
        """
        Cadastra um novo cliente com os dados inseridos nos campos.
        """
        # Obter dados dos campos
        nome = self.entry_nome.get().strip()
        cpf = self.entry_cpf.get().strip()
        telefone = self.entry_telefone.get().strip()
        email = self.entry_email.get().strip()
        
        # Validar campos obrigatórios
        if not all([nome, cpf, telefone, email]):
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return
        
        # Criar cliente e tentar adicionar
        cliente = Cliente(nome, cpf, telefone, email)
        
        if self.cadastro.adicionar_cliente(cliente):
            messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
            self.limpar_campos()
            self.listar_clientes()  # Atualizar a listagem
        else:
            messagebox.showerror("Erro", "Cliente com este CPF já existe!")
    
    def listar_clientes(self):
        """
        Exibe todos os clientes cadastrados na área de texto.
        """
        clientes = self.cadastro.listar_clientes()
        
        # Limpar área de texto
        self.text_listagem.delete(1.0, tk.END)
        
        if not clientes:
            self.text_listagem.insert(tk.END, "Nenhum cliente cadastrado.")
        else:
            self.text_listagem.insert(tk.END, f"Total de clientes: {len(clientes)}\n")
            self.text_listagem.insert(tk.END, "=" * 80 + "\n\n")
            
            for i, cliente in enumerate(clientes, 1):
                self.text_listagem.insert(tk.END, f"{i}. {cliente}\n\n")
    
    def remover_cliente(self):
        """
        Remove um cliente pelo CPF informado.
        """
        cpf = self.entry_cpf_remocao.get().strip()
        
        if not cpf:
            messagebox.showerror("Erro", "Informe o CPF para remoção!")
            return
        
        if self.cadastro.remover_cliente(cpf):
            messagebox.showinfo("Sucesso", "Cliente removido com sucesso!")
            self.entry_cpf_remocao.delete(0, tk.END)
            self.listar_clientes()  # Atualizar a listagem
        else:
            messagebox.showerror("Erro", "Cliente não encontrado!")
    
    def limpar_campos(self):
        """
        Limpa todos os campos de entrada de dados.
        """
        self.entry_nome.delete(0, tk.END)
        self.entry_cpf.delete(0, tk.END)
        self.entry_telefone.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
    
    def executar(self):
        """
        Inicia o loop principal da interface gráfica.
        """
        self.root.mainloop()
