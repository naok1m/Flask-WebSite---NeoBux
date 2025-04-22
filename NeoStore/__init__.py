from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"
app.config["SECRET_KEY"] = "353b65d35bf3eec7c38d507fba1b507f"


database = SQLAlchemy(app)
bcrypt = Bcrypt(app)




from NeoStore import views