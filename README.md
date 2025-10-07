# 🛒 NeoBux - Loja de Robux

Este é um projeto de uma loja virtual de **Robux**, a moeda do jogo Roblox, desenvolvida com o microframework **Flask**. A aplicação permite que usuários façam pedidos de Robux, preencham formulários e que os dados sejam salvos em um banco de dados SQLite.

## 🚀 Tecnologias utilizadas

- 🐍 **Python 3.7+**
- 🌐 **Flask 2.3.3**
- 🧠 **Flask-WTF** (validação de formulários)
- 🗃️ **SQLAlchemy** (ORM)
- 💾 **SQLite** (banco de dados)
- 🎨 **HTML + CSS**

## 📋 Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes do Python)

## 🚀 Instalação e Execução

### Método 1: Instalação Automática (Recomendado)

```bash
# 1. Navegue até a pasta do projeto
cd "C:\Users\thiago\Área de Trabalho\NeoBux\Flask-WebSite---NeoBux"

# 2. Execute o script de instalação
python instalar.py

# 3. Execute a aplicação
python main.py
```

### Método 2: Instalação Manual

```bash
# 1. Navegue até a pasta do projeto
cd "C:\Users\thiago\Área de Trabalho\NeoBux\Flask-WebSite---NeoBux"

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Crie o banco de dados
python criar_banco.py

# 4. Execute a aplicação
python main.py
```

## 🌐 Acesso

Após executar `python main.py`, acesse:

### 🏠 **Páginas Principais**
- **Loja**: http://localhost:5000
- **Pedidos**: http://localhost:5000/pedidos
- **Admin**: http://localhost:5000/admin/pedidos

### 📱 **URLs Importantes**
- **Homepage**: `/` - Loja principal
- **Pedidos Públicos**: `/pedidos` - Lista de pedidos recentes
- **Admin Dashboard**: `/admin/pedidos` - Painel administrativo
- **Status do Pedido**: `/pedido/<id>` - Acompanhar pedido específico

## ⚙️ Funcionalidades

### 🛒 **Loja Virtual**
- ✅ Página inicial moderna com design responsivo
- ✅ Catálogo de pacotes de Robux com preços
- ✅ Modal de compra com validação em tempo real
- ✅ Formulário de pedido com validação de email
- ✅ Sistema de pagamento via PIX simulado

### 📊 **Sistema de Pedidos**
- ✅ Criação automática de pedidos
- ✅ Sistema de status (Pendente → Verificado → Pago → Entregue)
- ✅ Página de acompanhamento de pedidos
- ✅ Timeline visual do progresso

### 🔧 **Painel Administrativo**
- ✅ Dashboard completo de pedidos
- ✅ Atualização de status em tempo real
- ✅ Estatísticas de vendas e faturamento
- ✅ Visualização detalhada de cada pedido
- ✅ Auto-refresh para acompanhamento contínuo

### 🎨 **Interface Moderna**
- ✅ Design responsivo para mobile e desktop
- ✅ Animações suaves e transições
- ✅ Notificações visuais
- ✅ Tema moderno com gradientes
- ✅ Ícones e emojis para melhor UX

### Campos do Formulário:
- Nome completo
- Username do Roblox
- E-mail
- Link do Gamepass

## 📁 Estrutura do Projeto

```
Flask-WebSite---NeoBux/
├── main.py                 # Arquivo principal
├── instalar.py            # Script de instalação automática
├── criar_banco.py         # Script para criar banco
├── requirements.txt       # Dependências
├── README.md             # Este arquivo
├── NeoStore/
│   ├── __init__.py       # Configuração do Flask
│   ├── models.py         # Modelos do banco
│   ├── views.py          # Rotas da aplicação
│   ├── forms.py          # Formulários
│   ├── static/css/       # Arquivos CSS
│   └── templates/        # Templates HTML
└── instance/
    └── comunidade.db     # Banco de dados SQLite
```

## 🛠️ Comandos Úteis

```bash
# Instalar dependências
pip install -r requirements.txt

# Criar/recriar banco de dados
python criar_banco.py

# Executar aplicação
python main.py

# Executar instalação completa
python instalar.py
```

## 🚧 Funcionalidades Futuras

- Sistema de autenticação de usuários
- Painel administrativo
- Sistema de pagamento
- Notificações por email
- API REST

## 🐛 Solução de Problemas

### Erro: "ModuleNotFoundError"
```bash
pip install -r requirements.txt
```

### Erro: "Database not found"
```bash
python criar_banco.py
```

### Erro: "Port already in use"
O Flask tentará usar uma porta alternativa automaticamente.

### Problemas com caracteres especiais no Windows
Use o PowerShell ou CMD com codificação UTF-8.

## 📞 Suporte

Se encontrar problemas, verifique:
1. Se o Python 3.7+ está instalado
2. Se todas as dependências foram instaladas
3. Se o banco de dados foi criado corretamente
4. Se não há outros serviços usando a porta 5000
