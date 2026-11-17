from app.extensions import db


class Produto(db.Model):
    __tablename__ = "produtos"

    __table_args__ = (
        db.UniqueConstraint(
            "categoria_id",
            "nome",
            name="uq_produto_categoria_nome"
        ),
    )

    id = db.Column(db.Integer, primary_key=True)

    categoria_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "categorias.id",
            ondelete="RESTRICT"
        ),
        nullable=False,
        index=True
    )

    nome = db.Column(
        db.String(120),
        nullable=False
    )

    descricao = db.Column(db.Text)

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

    categoria = db.relationship(
        "Categoria",
        back_populates="produtos"
    )

    variacoes = db.relationship(
        "VariacaoProduto",
        back_populates="produto"
    )

    def __repr__(self):
        return f"<Produto {self.nome}>"
