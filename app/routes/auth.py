
from urllib.parse import urljoin, urlparse

from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for
)

from flask_login import (
    current_user,
    login_user,
    logout_user
)

from sqlalchemy import select

from app.extensions import db
from app.forms.auth_forms import LoginForm, LogoutForm
from app.models import Usuario


auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/admin"
)


def destino_seguro(destino):
    if not destino:
        return False

    origem = urlparse(request.host_url)

    destino_url = urlparse(
        urljoin(request.host_url, destino)
    )

    return (
        destino_url.scheme in ("http", "https")
        and origem.netloc == destino_url.netloc
    )


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:
        return redirect(url_for("admin.dashboard"))

    form = LoginForm()

    if form.validate_on_submit():

        email = form.email.data.strip().casefold()

        usuario = db.session.scalar(
            select(Usuario).where(
                Usuario.email == email
            )
        )

        if (
            usuario
            and usuario.ativo
            and usuario.verificar_senha(form.senha.data)
        ):

            login_user(usuario)

            flash(
                "Bem-vindo ao painel administrativo!",
                "success"
            )

            destino = request.args.get("next")

            if destino_seguro(destino):
                return redirect(destino)

            return redirect(
                url_for("admin.dashboard")
            )

        flash(
            "E-mail ou senha inválidos.",
            "danger"
        )

    return render_template(
        "admin/login.html",
        form=form
    )


@auth_bp.route("/logout", methods=["POST"])
def logout():

    form = LogoutForm()

    if form.validate_on_submit():
        logout_user()

        flash(
            "Sessão encerrada com sucesso.",
            "success"
        )

    return redirect(url_for("auth.login"))
