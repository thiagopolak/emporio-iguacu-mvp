from app.extensions import db


class Categoria(db.Model):
    __tablename__ = "categorias"

    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column(
        db.String(80),
        nullable=False,
        unique=True
    )

    descricao = db.Column(db.String(255))

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

    produtos = db.relationship(
        "Produto",
        back_populates="categoria"
    )

    def __repr__(self):
        return f"<Categoria {self.nome}>"
