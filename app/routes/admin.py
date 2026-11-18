
from flask import Blueprint, render_template
from flask_login import login_required, current_user

from app.forms.auth_forms import LogoutForm


admin_bp = Blueprint(
    "admin",
    __name__,
    url_prefix="/admin"
)


@admin_bp.route("/")
@login_required
def dashboard():

    return render_template(
        "admin/dashboard.html",
        logout_form=LogoutForm()
    )
