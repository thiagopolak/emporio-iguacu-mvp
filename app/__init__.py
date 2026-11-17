
from flask import Flask

from config import Config
from app.extensions import db, migrate


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    # Inicializa as extensões
    db.init_app(app)
    migrate.init_app(app, db)

    # Registra os modelos no metadata do SQLAlchemy
    from app.models import (
        Categoria,
        Produto,
        VariacaoProduto
    )

    # Registra as rotas
    from app.routes.main import main_bp

    app.register_blueprint(main_bp)

    return app
