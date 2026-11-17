from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Extensão de acesso ao banco
db = SQLAlchemy()

# Gerenciamento de migrações
migrate = Migrate()
