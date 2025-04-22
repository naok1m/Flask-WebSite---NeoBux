from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, SelectField, HiddenField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError, URL




class FormPedido(FlaskForm):
    username = StringField('Nome de usuário no Roblox', validators=[DataRequired()])
    nome = StringField('Nome completo', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    linkgamepass = StringField('Link do Gamepass', validators=[DataRequired()])
    submit = SubmitField('Finalizar Pedido')
    # def validate_email(self):
    #     usuario = nick_roblox