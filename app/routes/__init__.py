
from flask import Flask

from config import Config
from app.extensions import db, migrate, login_manager


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    # Inicialização das extensões
    db.init_app(app)
    migrate.init_app(app, db)

    login_manager.init_app(app)

    login_manager.login_view = "auth.login"
    login_manager.login_message = (
        "Faça login para acessar esta área."
    )
    login_manager.login_message_category = "warning"
    login_manager.session_protection = "strong"

    # Registro dos modelos
    from app.models import (
        Categoria,
        Produto,
        VariacaoProduto,
        Usuario
    )

    # Recuperação do usuário pela sessão
    @login_manager.user_loader
    def carregar_usuario(user_id):

        try:
            return db.session.get(
                Usuario,
                int(user_id)
            )
        except (TypeError, ValueError):
            return None

    # Registro das rotas
    from app.routes.main import main_bp
    from app.routes.auth import auth_bp
    from app.routes.admin import admin_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)

    return app
