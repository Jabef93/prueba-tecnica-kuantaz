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
    return app


""" if __name__ == '__main__':
    app.config.from_object(config['development'])
    

    # blueprints
    app.register_blueprint(Instituciones.main, url_prefix='/api/instituciones/list')

    # error handling
    app.register_error_handler(404, page_not_found)
    app.run()
 """