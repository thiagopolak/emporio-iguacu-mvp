
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):

    email = StringField(
        "E-mail",
        validators=[
            DataRequired(),
            Length(max=120)
        ],
        render_kw={
            "type": "email",
            "autocomplete": "username",
            "placeholder": "Digite seu e-mail"
        }
    )

    senha = PasswordField(
        "Senha",
        validators=[
            DataRequired()
        ],
        render_kw={
            "autocomplete": "current-password",
            "placeholder": "Digite sua senha"
        }
    )

    submit = SubmitField("Entrar")


class LogoutForm(FlaskForm):
    submit = SubmitField("Sair")
