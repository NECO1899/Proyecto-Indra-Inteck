from flask import Blueprint, render_template, session, redirect, url_for

activos_bp = Blueprint("activos", __name__, url_prefix="/sistema")

@activos_bp.route("/index")
def index():
    if "usuario" not in session:
        return redirect(url_for("auth.login"))

    return render_template("index.html")

@activos_bp.route("/ingreso")
def ingreso_activos():
    return render_template("ingreso.html")

@activos_bp.route('/depuracion')
def depuracion():
    return render_template('Depuracion.html')

@activos_bp.route("/salida_solicitante")
def salida_solicitante():
    return render_template("Salida_Solicitante.html")

@activos_bp.route("/salida_aprobacion")
def salida_aprobacion():
    return render_template("Salida_Aprobacion.html")

@activos_bp.route("/salida_seguridad")
def salida_seguridad():
    return render_template("Salida_Seguridad.html")

@activos_bp.route("/registro_visitantes")
def registro_visitantes():
    return render_template("Visitantes_Registro.html")


@activos_bp.route("/consulta")
def consulta():
    return render_template("Consulta.html")

@activos_bp.route("/informes")
def informes():
    return render_template("Informes.html")