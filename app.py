from flask import Flask
from controllers.auth_controller import auth_bp
from controllers.activos_controller import activos_bp

app = Flask(__name__)
app.secret_key = "clave_super_segura"

app.register_blueprint(auth_bp)
app.register_blueprint(activos_bp)

if __name__ == "__main__":
    app.run(debug=True)