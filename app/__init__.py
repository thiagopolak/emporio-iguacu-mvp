
from flask import Flask

from config import Config
from app.extensions import db


def create_app():
    app = Flask(__name__)

    # Carrega as configurações
    app.config.from_object(Config)

    # Inicializa o banco de dados
    db.init_app(app)

    # Registra as rotas principais
    from app.routes.main import main_bp

    app.register_blueprint(main_bp)

    return app
