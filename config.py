import os

from dotenv import load_dotenv
from sqlalchemy import URL

load_dotenv()

# Monta a URL de conexão com segurança,
# inclusive quando a senha possui caracteres especiais.
database_url = URL.create(
    drivername="postgresql+psycopg",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST", "localhost"),
    port=int(os.getenv("DB_PORT", "5432")),
    database=os.getenv("DB_NAME", "emporio_iguacu"),
)


class Config:
    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "dev-only-change-before-production"
    )

    SQLALCHEMY_DATABASE_URI = database_url

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DEBUG = os.getenv(
        "FLASK_DEBUG", "false"
    ).lower() in ("true", "1", "yes")
