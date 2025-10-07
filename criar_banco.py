from NeoStore import database, app
from NeoStore.models import Produto, Pedido

def criar_banco():
    """Cria o banco de dados e as tabelas necessárias"""
    with app.app_context():
        # Criar todas as tabelas
        database.create_all()
        
        # Verificar se já existem produtos
        if Produto.query.count() == 0:
            # Criar produtos iniciais
            produtos_iniciais = [
                Produto(nome="Pacote 100 Robux", quantidade=100, preco=5.99),
                Produto(nome="Pacote 400 Robux", quantidade=400, preco=19.99),
                Produto(nome="Pacote 800 Robux", quantidade=800, preco=34.99),
                Produto(nome="Pacote 1700 Robux", quantidade=1700, preco=69.99),
            ]
            
            for produto in produtos_iniciais:
                database.session.add(produto)
            
            database.session.commit()
            print("✅ Banco de dados criado com sucesso!")
            print("✅ Produtos iniciais adicionados!")
        else:
            print("✅ Banco de dados já existe!")

if __name__ == "__main__":
    criar_banco()