from app.extensions import db


class VariacaoProduto(db.Model):
    __tablename__ = "variacoes_produtos"

    __table_args__ = (
        db.UniqueConstraint(
            "produto_id",
            "nome",
            name="uq_variacao_produto_nome"
        ),
        db.CheckConstraint(
            "preco > 0",
            name="ck_variacao_preco_positivo"
        ),
        db.CheckConstraint(
            "unidade_venda IN ('kg', 'unidade')",
            name="ck_variacao_unidade_valida"
        ),
    )

    id = db.Column(db.Integer, primary_key=True)

    produto_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "produtos.id",
            ondelete="RESTRICT"
        ),
        nullable=False,
        index=True
    )

    nome = db.Column(
        db.String(100),
        nullable=False
    )

    preco = db.Column(
        db.Numeric(10, 2),
        nullable=False
    )

    unidade_venda = db.Column(
        db.String(20),
        nullable=False
    )

    ativo = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )

    produto = db.relationship(
        "Produto",
        back_populates="variacoes"
    )

    def __repr__(self):
        return f"<VariacaoProduto {self.nome}>"
