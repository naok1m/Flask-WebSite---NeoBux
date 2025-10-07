from flask import render_template, url_for, request, redirect # pegue a url de acordo com a def
import requests
from NeoStore import app
from NeoStore.forms import FormPedido
from NeoStore.models import Produto, database, Pedido
from datetime import datetime
# Rotas


@app.route('/', methods=["GET", "POST"])
def homepage():
    # Criar produtos iniciais se não houver nenhum
    if Produto.query.count() == 0:
        produtos = [
            Produto(nome="Pacote 100 Robux", quantidade=100, preco=5.99),
            Produto(nome="Pacote 400 Robux", quantidade=400, preco=19.99),
            Produto(nome="Pacote 800 Robux", quantidade=800, preco=34.99),
            Produto(nome="Pacote 1700 Robux", quantidade=1700, preco=69.99),
        ]
        for produto in produtos:
            database.session.add(produto)
        database.session.commit()

    form = FormPedido()

    if request.method == "POST":
        if form.validate_on_submit():
            produto_id = request.form.get("produto")
            produto = Produto.query.get(produto_id)

            if produto:
                novo_pedido = Pedido(
                    nick_roblox=form.username.data,
                    nome_comprador=form.nome.data,
                    email_comprador=form.email.data,
                    gamepass_link=form.linkgamepass.data,
                    produto_id=produto.id,
                    data_pedido=datetime.utcnow(),
                    status="pendente"
                )
                database.session.add(novo_pedido)
                database.session.commit()

                print(f"Pedido criado com sucesso: {novo_pedido.id}")
                return redirect(url_for('ver_pedido', pedido_id=novo_pedido.id))
            else:
                print("Produto não encontrado.")
        else:
            print("Formulário não validado.")

    produtos = Produto.query.all()
    return render_template('homepage.html', produtos=produtos, form=form)


from flask import jsonify

@app.route('/pedido/<int:pedido_id>')
def ver_pedido(pedido_id):
    pedido = Pedido.query.get_or_404(pedido_id)
    return render_template('status_pedido.html', pedido=pedido)

@app.route('/admin/pedidos')
def admin_pedidos():
    """Página administrativa para visualizar pedidos"""
    lista_pedidos = Pedido.query.order_by(Pedido.data_pedido.desc()).all()
    return render_template('admin_pedidos.html', pedidos=lista_pedidos)

@app.route('/admin/atualizar-status/<int:pedido_id>', methods=['POST'])
def atualizar_status_pedido(pedido_id):
    """Atualiza o status de um pedido"""
    pedido = Pedido.query.get_or_404(pedido_id)
    novo_status = request.form.get('status')
    
    if novo_status in ['pendente', 'verificado', 'pago', 'entregue', 'cancelado']:
        pedido.status = novo_status
        database.session.commit()
        print(f"Status do pedido {pedido_id} atualizado para: {novo_status}")
    
    return redirect(url_for('admin_pedidos'))

@app.route('/pedidos')
def pedidos():
    """Página pública para visualizar pedidos (apenas status)"""
    lista_pedidos = Pedido.query.order_by(Pedido.data_pedido.desc()).limit(10).all()
    return render_template('pedidos.html', pedidos=lista_pedidos)



# Rotas adicionais podem ser adicionadas aqui



