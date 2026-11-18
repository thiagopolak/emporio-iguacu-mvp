
from getpass import getpass

from sqlalchemy import select

from app import create_app
from app.extensions import db
from app.models import Usuario


def criar_admin():

    nome = input("Nome do administrador: ").strip()
    email = input("E-mail do administrador: ").strip().casefold()

    if not nome or "@" not in email:
        print("Nome ou e-mail inválido.")
        return

    senha = getpass("Digite uma senha (mínimo 12 caracteres): ")
    confirmacao = getpass("Confirme a senha: ")

    if senha != confirmacao:
        print("As senhas não conferem.")
        return

    if len(senha) < 12:
        print("A senha precisa ter pelo menos 12 caracteres.")
        return

    app = create_app()

    with app.app_context():

        existente = db.session.scalar(
            select(Usuario).where(
                Usuario.email == email
            )
        )

        if existente:
            print("Já existe um usuário com esse e-mail.")
            return

        usuario = Usuario(
            nome=nome,
            email=email,
            ativo=True
        )

        usuario.definir_senha(senha)

        db.session.add(usuario)

        try:
            db.session.commit()
            print("Administrador cadastrado com sucesso!")

        except Exception:
            db.session.rollback()
            print("Não foi possível cadastrar o administrador.")
            raise


if __name__ == "__main__":
    criar_admin()
