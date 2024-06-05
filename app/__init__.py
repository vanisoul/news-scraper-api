from flask import Flask
from flasgger import Swagger

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    Swagger(app)

    from .routes import main
    app.register_blueprint(main)

    return app
