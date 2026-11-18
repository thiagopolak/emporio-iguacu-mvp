
from argon2 import PasswordHasher
from argon2.exceptions import VerificationError
from flask_login import UserMixin

from app.extensions import db


password_hasher = PasswordHasher()


class Usuario(UserMixin, db.Model):
    __tablename__ = "usuarios"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nome = db.Column(
        db.String(120),
        nullable=False
    )

    email = db.Column(
        db.String(120),
        nullable=False,
        unique=True,
        index=True
    )

    senha_hash = db.Column(
        db.String(255),
        nullable=False
    )

    ativo = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )

    criado_em = db.Column(
        db.DateTime(timezone=True),
        nullable=False,
        server_default=db.func.now()
    )

    @property
    def is_active(self):
        return self.ativo

    def definir_senha(self, senha):
        if len(senha) < 12:
            raise ValueError(
                "A senha deve possuir pelo menos 12 caracteres."
            )

        self.senha_hash = password_hasher.hash(senha)

    def verificar_senha(self, senha):
        try:
            return password_hasher.verify(
                self.senha_hash,
                senha
            )
        except VerificationError:
            return False

    def __repr__(self):
        return f"<Usuario {self.email}>"
