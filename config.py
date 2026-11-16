
import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "chave-temporaria-apenas-desenvolvimento"
    )

    DEBUG = os.getenv("FLASK_DEBUG", "true").lower() in (
        "true", "1", "yes"
    )
