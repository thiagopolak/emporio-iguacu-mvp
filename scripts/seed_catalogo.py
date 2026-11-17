
from decimal import Decimal

from sqlalchemy import select

from app import create_app
from app.extensions import db
from app.models import Categoria, Produto, VariacaoProduto


# Catálogo inicial do Empório Iguaçu.
# Preços armazenados como Decimal para preservar precisão monetária.
# Produtos sem unidade informada foram provisoriamente
# configurados como kg, sujeitos à confirmação da loja.

CATALOGO = [
    {
        "categoria": "Castanhas e oleaginosas",
        "descricao": "Castanhas e oleaginosas em diferentes preparos.",
        "produtos": [
            {
                "nome": "Castanha de caju",
                "descricao": "Castanha de caju em diferentes preparos.",
                "variacoes": [
                    ("Torrada com sal", "90.00", "kg"),
                    ("Torrada sem sal", "90.00", "kg"),
                    ("Crua", "90.00", "kg"),
                    ("Xerém (granulada)", "75.00", "kg"),
                    ("Moída (farinha)", "75.00", "kg"),
                ],
            },
            {
                "nome": "Amêndoa",
                "descricao": "Amêndoas em diferentes preparos.",
                "variacoes": [
                    ("Torrada com sal", "80.00", "kg"),
                    ("Torrada sem sal", "80.00", "kg"),
                    ("Defumada", "65.00", "kg"),
                    ("Crua", "80.00", "kg"),
                    ("Laminada", "95.00", "kg"),
                    ("Farinha", "85.00", "kg"),
                ],
            },
            {
                "nome": "Castanha do Pará",
                "descricao": "Castanha do Pará inteira, quebrada ou em farinha.",
                "variacoes": [
                    ("Inteira", "90.00", "kg"),
                    ("Quebrada", "75.00", "kg"),
                    ("Farinha", "70.00", "kg"),
                ],
            },
            {
                "nome": "Nozes chilena",
                "descricao": "Nozes chilenas em diferentes apresentações.",
                "variacoes": [
                    ("Inteira", "75.00", "kg"),
                    ("Quebrada", "58.00", "kg"),
                ],
            },
        ],
    },
    {
        "categoria": "Frutas secas",
        "descricao": "Frutas secas selecionadas para venda a granel.",
        "produtos": [
            {
                "nome": "Ameixa preta",
                "descricao": "Ameixa preta sem caroço.",
                "variacoes": [
                    ("Sem caroço", "40.00", "kg"),
                ],
            },
            {
                "nome": "Uva passa preta",
                "descricao": "Uva passa preta sem caroço.",
                "variacoes": [
                    ("Sem caroço", "20.00", "kg"),
                ],
            },
            {
                "nome": "Uva passa branca",
                "descricao": "Uva passa branca sem caroço.",
                "variacoes": [
                    ("Sem caroço", "35.00", "kg"),
                ],
            },
            {
                "nome": "Damasco turco",
                "descricao": "Damasco turco.",
                "variacoes": [
                    ("Tradicional", "90.00", "kg"),
                ],
            },
        ],
    },
    {
        "categoria": "Coco e derivados",
        "descricao": "Produtos de coco fresco e derivados.",
        "produtos": [
            {
                "nome": "Coco fresco",
                "descricao": "Coco fresco em diferentes cortes.",
                "variacoes": [
                    ("Ralado fino", "35.00", "kg"),
                    ("Ralado médio", "35.00", "kg"),
                    ("Ralado grosso", "35.00", "kg"),
                    ("Inteiro", "35.00", "kg"),
                ],
            },
            {
                "nome": "Coco fresco em fita",
                "descricao": "Coco fresco cortado em formato de fita.",
                "variacoes": [
                    ("Com pele", "50.00", "kg"),
                    ("Sem pele", "50.00", "kg"),
                ],
            },
        ],
    },
]


def obter_ou_criar_categoria(nome, descricao):
    categoria = db.session.scalar(
        select(Categoria).where(Categoria.nome == nome)
    )

    if categoria is None:
        categoria = Categoria(
            nome=nome,
            descricao=descricao,
            ativo=True,
        )
        db.session.add(categoria)
        db.session.flush()

    return categoria


def obter_ou_criar_produto(categoria, dados):
    produto = db.session.scalar(
        select(Produto).where(
            Produto.categoria_id == categoria.id,
            Produto.nome == dados["nome"],
        )
    )

    if produto is None:
        produto = Produto(
            categoria_id=categoria.id,
            nome=dados["nome"],
            descricao=dados["descricao"],
            ativo=True,
        )
        db.session.add(produto)
        db.session.flush()

    else:
        produto.descricao = dados["descricao"]
        produto.ativo = True

    return produto


def obter_ou_atualizar_variacao(produto, dados):
    nome, preco, unidade = dados

    variacao = db.session.scalar(
        select(VariacaoProduto).where(
            VariacaoProduto.produto_id == produto.id,
            VariacaoProduto.nome == nome,
        )
    )

    if variacao is None:
        variacao = VariacaoProduto(
            produto_id=produto.id,
            nome=nome,
            preco=Decimal(preco),
            unidade_venda=unidade,
            ativo=True,
        )
        db.session.add(variacao)

    else:
        variacao.preco = Decimal(preco)
        variacao.unidade_venda = unidade
        variacao.ativo = True


def carregar_catalogo():
    total_categorias = 0
    total_produtos = 0
    total_variacoes = 0

    try:
        for dados_categoria in CATALOGO:

            categoria = obter_ou_criar_categoria(
                dados_categoria["categoria"],
                dados_categoria["descricao"],
            )

            total_categorias += 1

            for dados_produto in dados_categoria["produtos"]:

                produto = obter_ou_criar_produto(
                    categoria,
                    dados_produto,
                )

                total_produtos += 1

                for dados_variacao in dados_produto["variacoes"]:

                    obter_ou_atualizar_variacao(
                        produto,
                        dados_variacao,
                    )

                    total_variacoes += 1

        db.session.commit()

        print("\nCatálogo carregado com sucesso!")
        print(f"Categorias processadas: {total_categorias}")
        print(f"Produtos processados: {total_produtos}")
        print(f"Variações processadas: {total_variacoes}")

    except Exception:
        db.session.rollback()
        raise


if __name__ == "__main__":
    app = create_app()

    with app.app_context():
        carregar_catalogo()
