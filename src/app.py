from flask import Flask

from config import config
from routes import Instituciones

app = Flask(__name__)


def page_not_found(error):
    return "<h1>Page Not Found</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])

    # blueprints
    app.register_blueprint(Instituciones.main, url_prefix='/api/instituciones/list')

    # error handling
    app.register_error_handler(404, page_not_found)
    app.run()
