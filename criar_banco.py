from NeoStore import database, app
from NeoStore.models import Produto, Pedido

with app.app_context():
    database.create_all()