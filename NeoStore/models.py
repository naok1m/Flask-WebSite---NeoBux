# criar estrutura do banco de dados
from datetime import datetime
from NeoStore import database
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy




class Produto(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String(100), nullable=False)  # ex: Pacote de 800 ROBUX
    quantidade = database.Column(database.Integer, nullable=False)  # quantidade de Robux
    preco = database.Column(database.Float, nullable=False)  # preço em R$

    def __repr__(self):
        return f"Produto('{self.nome}', {self.quantidade} Robux, R${self.preco})"


class Pedido(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    produto_id = database.Column(database.Integer, database.ForeignKey('produto.id'), nullable=False)
    nick_roblox = database.Column(database.String(100), nullable=False)
    nome_comprador = database.Column(database.String(100), nullable=False)
    email_comprador = database.Column(database.String(120), nullable=False)
    gamepass_link = database.Column(database.String(255), nullable=False)
    data_pedido = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    status = database.Column(database.String(20), nullable=False, default='pendente')  # pendente, verificado, pago, entregue, cancelado
    
    
    produto = database.relationship('Produto', backref=database.backref('pedidos', lazy=True))

    def __repr__(self):
        return f"Pedido('{self.nick_roblox}', '{self.produto.nome}', '{self.status}')"