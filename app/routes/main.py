
from flask import Blueprint, render_template

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    produtos = [
        {
            "nome": "Castanha de caju salgada",
            "categoria": "Castanhas",
            "preco": 89.90,
            "unidade": "kg",
            "descricao": "Castanha selecionada e torrada com sal."
        },
        {
            "nome": "Amêndoa crua",
            "categoria": "Castanhas",
            "preco": 79.90,
            "unidade": "kg",
            "descricao": "Amêndoas inteiras e naturais."
        },
        {
            "nome": "Farinha de aveia",
            "categoria": "Farinhas",
            "preco": 18.90,
            "unidade": "kg",
            "descricao": "Farinha fina e ideal para receitas."
        }
    ]

    return render_template(
        "index.html",
        produtos=produtos
    )
