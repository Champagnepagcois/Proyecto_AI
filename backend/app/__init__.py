from flask import Flask
from app.routes import users
from app.database import init_db

def create_app():
    app = Flask(__name__)

    # Configuración de la base de datos
    app.config.from_object("app.config.Config")
    init_db(app)

    # Registro de rutas (blueprints)
    app.register_blueprint(users.bp)

    return app
