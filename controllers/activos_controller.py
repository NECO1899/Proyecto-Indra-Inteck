from flask import Blueprint, render_template, session, redirect, url_for

activos_bp = Blueprint("activos", __name__, url_prefix="/sistema")

@activos_bp.route("/index")
def index():
    if "usuario" not in session:
        return redirect(url_for("auth.login"))

    return render_template("index.html")