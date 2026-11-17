
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.extensions import db
from app.models import Categoria, Produto, VariacaoProduto


def listar_categorias_com_produtos():
    """
    Retorna categorias ativas com seus produtos
    e respectivas variações também ativas.
    """

    consulta = (
        select(Categoria)
        .where(Categoria.ativo.is_(True))
        .options(
            selectinload(
                Categoria.produtos.and_(
                    Produto.ativo.is_(True)
                )
            ).selectinload(
                Produto.variacoes.and_(
                    VariacaoProduto.ativo.is_(True)
                )
            )
        )
        .order_by(Categoria.nome)
    )

    resultado = db.session.scalars(consulta).all()

    return resultado
