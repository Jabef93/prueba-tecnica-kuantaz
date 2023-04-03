from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.config import config

db = SQLAlchemy()

def page_not_found(error):
    return "<h1>Page Not Found</h1>", 404


def create_app():
    app = Flask(__name__)
    app.config.from_object(config['development'])
    db.init_app(app)

    from .models import Instituciones, Proyectos, Usuarios

    with app.app_context():
        db.create_all()

    from app.routes.instituciones import instituciones
    from app.routes.usuarios import usuarios
    from app.routes.proyectos import proyectos
    app.register_blueprint(instituciones)
    app.register_blueprint(usuarios)
    app.register_blueprint(proyectos)
    
    return app
