from flask import Blueprint, render_template, request, redirect, url_for, session, flash

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/")
def login():
    return render_template("login.html")

@auth_bp.route("/validar", methods=["POST"])
def validar():
    usuario = request.form["usuario"]
    clave = request.form["clave"]

    if usuario == "admin" and clave == "1234":
        session.clear()
        session["usuario"] = usuario
        session["rol"] = "admin"
        return redirect(url_for("activos.index"))

    flash("Usuario o contraseña incorrectos", "error")
    return render_template("login.html")

@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))