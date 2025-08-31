# PyMath - Calculadora Python

Uma calculadora simples implementada em Python que oferece operações matemáticas básicas e avançadas através de uma interface de linha de comando.

## 📝 Descrição

O PyMath é uma aplicação de calculadora que permite aos usuários realizar:

### Operações Aritméticas Básicas
- **Adição**: Soma de dois números
- **Subtração**: Diferença entre dois números
- **Multiplicação**: Produto de dois números
- **Divisão**: Quociente de dois números (com tratamento de divisão por zero)

### Operações Avançadas
- **Potenciação**: Elevação de um número a uma potência
- **Radiciação**: Cálculo de raízes (raiz n-ésima)

## 🚀 Como Executar

### Pré-requisitos
- Python 3.x instalado no sistema

### Executando o Projeto

O projeto possui dois módulos principais que podem ser executados independentemente:

#### 1. Calculadora de Operações Básicas
```bash
python calculations/basic_arithmetic_operations.py
```

#### 2. Calculadora de Potenciação e Radiciação
```bash
python calculations/exponentiation_and_root.py
```

### Como Usar

1. Execute um dos comandos acima
2. Escolha a operação desejada digitando o número correspondente
3. Digite os números quando solicitado
4. Veja o resultado da operação
5. Escolha se deseja continuar ou sair do programa

## 📁 Estrutura do Projeto

```
PyMath/
├── calculations/
│   ├── basic_arithmetic_operations.py    # Operações básicas (+, -, *, /)
│   └── exponentiation_and_root.py        # Potenciação e radiciação
├── utils/
│   ├── menu_functions.py                 # Funções de exibição de menus
│   └── user_choices.py                   # Funções de captura de entrada do usuário
├── .gitignore                            # Arquivos ignorados pelo Git
└── README.md                             # Este arquivo
```

## 🔧 Funcionalidades

### Operações Básicas
- Interface intuitiva com menu numerado
- Validação de entrada do usuário
- Tratamento de erros (divisão por zero, valores inválidos)
- Opção de continuar ou sair após cada operação

### Operações Avançadas
- Cálculo de potências (a^b)
- Cálculo de raízes (a^(1/b))
- Interface similar às operações básicas

## 🛡️ Tratamento de Erros

O projeto inclui tratamento robusto de erros:
- **Divisão por zero**: Exibe mensagem de erro apropriada
- **Valores inválidos**: Solicita entrada válida quando números não numéricos são inseridos
- **Opções inválidas**: Reexibe o menu quando opções inválidas são selecionadas

## 🤝 Contribuindo

Para contribuir com o projeto:
1. Faça um fork do repositório
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📄 Licença

Este projeto é open source e está disponível sob a [MIT License](LICENSE).

---

**PyMath** - Uma calculadora Python simples e eficiente para operações matemáticas básicas e avançadas.