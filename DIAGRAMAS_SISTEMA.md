# Diagramas do Sistema de Cadastro de Clientes

## 1. Diagrama de Classes UML

\`\`\`
┌─────────────────────────────────┐
│            Cliente              │
├─────────────────────────────────┤
│ - nome: str                     │
│ - cpf: str                      │
│ - telefone: str                 │
│ - email: str                    │
├─────────────────────────────────┤
│ + __init__(nome, cpf, tel, email)│
│ + __str__(): str                │
│ + __repr__(): str               │
└─────────────────────────────────┘
                 ▲
                 │ 1..*
                 │ (composição)
                 │
┌─────────────────────────────────┐
│        CadastroClientes         │
├─────────────────────────────────┤
│ - _clientes: List[Cliente]      │
├─────────────────────────────────┤
│ + __init__()                    │
│ + adicionar_cliente(Cliente): bool│
│ + listar_clientes(): List[Cliente]│
│ + buscar_cliente_por_cpf(str): Cliente│
│ + remover_cliente(str): bool    │
│ + total_clientes(): int         │
└─────────────────────────────────┘
                 ▲
                 │ 1
                 │ (agregação)
                 │
┌─────────────────────────────────┐
│       InterfaceGrafica          │
├─────────────────────────────────┤
│ - cadastro: CadastroClientes    │
│ - root: tk.Tk                   │
│ - entry_nome: ttk.Entry         │
│ - entry_cpf: ttk.Entry          │
│ - entry_telefone: ttk.Entry     │
│ - entry_email: ttk.Entry        │
│ - entry_cpf_remocao: ttk.Entry  │
│ - text_listagem: ScrolledText   │
├─────────────────────────────────┤
│ + __init__()                    │
│ + configurar_janela()           │
│ + criar_widgets()               │
│ + criar_frame_entrada(parent)   │
│ + criar_frame_botoes(parent)    │
│ + criar_frame_listagem(parent)  │
│ + criar_frame_remocao(parent)   │
│ + cadastrar_cliente()           │
│ + listar_clientes()             │
│ + remover_cliente()             │
│ + limpar_campos()               │
│ + executar()                    │
└─────────────────────────────────┘
\`\`\`

## 2. Diagrama de Arquitetura do Sistema

\`\`\`
┌─────────────────────────────────────────────────────────────┐
│                    SISTEMA DESKTOP                          │
│                                                             │
│  ┌─────────────────┐    ┌─────────────────┐                │
│  │   main.py       │    │  test_sistema.py│                │
│  │                 │    │                 │                │
│  │ • Ponto entrada │    │ • Testes        │                │
│  │ • Inicialização │    │ • Validação     │                │
│  └─────────────────┘    └─────────────────┘                │
│           │                                                 │
│           ▼                                                 │
│  ┌─────────────────────────────────────────────────────────┐│
│  │              CAMADA DE APRESENTAÇÃO                     ││
│  │                                                         ││
│  │  ┌─────────────────────────────────────────────────────┐││
│  │  │           InterfaceGrafica                          │││
│  │  │                                                     │││
│  │  │ • Tkinter GUI                                       │││
│  │  │ • Formulários de entrada                            │││
│  │  │ • Botões de ação                                    │││
│  │  │ • Área de listagem                                  │││
│  │  │ • Validação de entrada                              │││
│  │  └─────────────────────────────────────────────────────┘││
│  └─────────────────────────────────────────────────────────┘│
│           │                                                 │
│           ▼                                                 │
│  ┌─────────────────────────────────────────────────────────┐│
│  │               CAMADA DE NEGÓCIO                         ││
│  │                                                         ││
│  │  ┌─────────────────────────────────────────────────────┐││
│  │  │           CadastroClientes                          │││
│  │  │                                                     │││
│  │  │ • Gerenciamento de clientes                         │││
│  │  │ • Operações CRUD                                    │││
│  │  │ • Validação de CPF                                  │││
│  │  │ • Busca e filtragem                                 │││
│  │  └─────────────────────────────────────────────────────┘││
│  └─────────────────────────────────────────────────────────┘│
│           │                                                 │
│           ▼                                                 │
│  ┌─────────────────────────────────────────────────────────┐│
│  │               CAMADA DE DADOS                           ││
│  │                                                         ││
│  │  ┌─────────────────────────────────────────────────────┐││
│  │  │                Cliente                              │││
│  │  │                                                     │││
│  │  │ • Modelo de dados                                   │││
│  │  │ • Atributos do cliente                              │││
│  │  │ • Representação de objetos                          │││
│  │  └─────────────────────────────────────────────────────┘││
│  │                                                         ││
│  │  ┌─────────────────────────────────────────────────────┐││
│  │  │            Armazenamento                            │││
│  │  │                                                     │││
│  │  │ • Lista em memória                                  │││
│  │  │ • Estrutura de dados Python                        │││
│  │  └─────────────────────────────────────────────────────┘││
│  └─────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────┘
\`\`\`

## 3. Fluxo de Dados e Interações

\`\`\`
┌─────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Usuário   │───▶│ InterfaceGrafica│───▶│CadastroClientes │
└─────────────┘    └─────────────────┘    └─────────────────┘
       ▲                    │                       │
       │                    │                       ▼
       │                    │              ┌─────────────────┐
       │                    │              │    Cliente      │
       │                    │              │   (Objetos)     │
       │                    │              └─────────────────┘
       │                    │                       │
       │                    ▼                       │
       │           ┌─────────────────┐              │
       └───────────│   Feedback      │◀─────────────┘
                   │   Visual        │
                   └─────────────────┘
\`\`\`

## 4. Padrões de Design Utilizados

### MVC (Model-View-Controller)
- **Model**: Cliente (dados)
- **View**: InterfaceGrafica (apresentação)
- **Controller**: CadastroClientes (lógica de negócio)

### Encapsulamento
- Atributos privados em CadastroClientes (`_clientes`)
- Métodos públicos para acesso controlado

### Composição
- CadastroClientes contém uma lista de objetos Cliente
- Relacionamento forte entre as classes

## 5. Tecnologias e Ferramentas

\`\`\`
┌─────────────────────────────────────────────────────────────┐
│                    STACK TECNOLÓGICO                        │
├─────────────────────────────────────────────────────────────┤
│ Linguagem: Python 3.x                                      │
│ GUI Framework: Tkinter                                      │
│ Paradigma: Programação Orientada a Objetos                 │
│ Armazenamento: Memória (Listas Python)                     │
│ Testes: Unittest                                            │
│ Documentação: Markdown                                      │
│ Controle de Versão: Git/GitHub                             │
└─────────────────────────────────────────────────────────────┘
