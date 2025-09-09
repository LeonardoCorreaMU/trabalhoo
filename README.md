# Sistema de Cadastro de Clientes

## Descrição

Este projeto implementa um sistema desktop para cadastro e gerenciamento de clientes, desenvolvido em Python utilizando a biblioteca Tkinter para interface gráfica. O sistema foi criado seguindo os princípios da Programação Orientada a Objetos (POO).

## Funcionalidades

- ✅ Cadastrar novos clientes com nome, CPF, telefone e email
- ✅ Listar todos os clientes cadastrados
- ✅ Remover clientes pelo CPF
- ✅ Interface gráfica intuitiva e responsiva
- ✅ Validação de dados de entrada
- ✅ Prevenção de CPFs duplicados

## Estrutura do Projeto

\`\`\`
projeto/
├── main.py                 # Arquivo principal para executar o sistema
├── cliente.py              # Classe Cliente
├── cadastro_clientes.py    # Classe CadastroClientes
├── interface_grafica.py    # Interface gráfica com Tkinter
├── test_sistema.py         # Testes básicos do sistema
└── README.md              # Documentação do projeto
\`\`\`

## Classes Implementadas

### Cliente
Representa um cliente do sistema com os seguintes atributos:
- `nome`: Nome completo do cliente
- `cpf`: CPF do cliente
- `telefone`: Telefone de contato
- `email`: Email do cliente

### CadastroClientes
Gerencia as operações CRUD dos clientes:
- `adicionar_cliente()`: Adiciona um novo cliente
- `listar_clientes()`: Retorna lista de todos os clientes
- `buscar_cliente_por_cpf()`: Busca cliente por CPF
- `remover_cliente()`: Remove cliente pelo CPF
- `total_clientes()`: Retorna número total de clientes

### InterfaceGrafica
Implementa a interface gráfica usando Tkinter com:
- Formulário para entrada de dados
- Botões para ações (cadastrar, listar, limpar)
- Área de texto para exibir clientes
- Campo para remoção por CPF

## Como Executar

### Pré-requisitos
- Python 3.7 ou superior
- Tkinter (geralmente incluído com Python)

### Instalação e Execução

1. Clone ou baixe o projeto
2. Navegue até a pasta do projeto
3. Execute o sistema:

\`\`\`bash
python main.py
\`\`\`

### Executar Testes

Para executar os testes básicos:

\`\`\`bash
python test_sistema.py
\`\`\`

## Ambiente Virtual (Opcional)

Para criar um ambiente virtual isolado:

\`\`\`bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Executar o sistema
python main.py
\`\`\`

## Conceitos de POO Aplicados

### Encapsulamento
- Atributos privados na classe `CadastroClientes` (prefixo `_`)
- Métodos públicos para acesso controlado aos dados

### Abstração
- Classes representam entidades do mundo real (Cliente, Cadastro)
- Interface simplificada para operações complexas

### Modularidade
- Separação de responsabilidades em diferentes classes
- Código organizado em módulos específicos

## Validações Implementadas

- ✅ Verificação de campos obrigatórios
- ✅ Prevenção de CPFs duplicados
- ✅ Mensagens de erro e sucesso
- ✅ Limpeza automática de campos após cadastro

## Melhorias Futuras

- [ ] Persistência de dados em arquivo ou banco de dados
- [ ] Validação de formato de CPF e email
- [ ] Edição de clientes existentes
- [ ] Busca por nome ou outros campos
- [ ] Exportação de dados para CSV/Excel
- [ ] Backup automático dos dados

## Tecnologias Utilizadas

- **Python 3**: Linguagem de programação principal
- **Tkinter**: Biblioteca para interface gráfica
- **POO**: Paradigma de programação orientada a objetos

## Autor

Sistema desenvolvido para atividade acadêmica sobre desenvolvimento de software desktop com Python e POO.

## Licença

Este projeto é destinado para fins educacionais.
