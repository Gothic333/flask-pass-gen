from flask import Flask
from config import config as Config


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(Config[config_name])
    Config[config_name].init_app(app)

    from .blueprints.home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .blueprints.passphrase import passphrase as passphrase_blueprint
    app.register_blueprint(passphrase_blueprint)

    from .blueprints.simplepass import simplepass as simplepass_blueprint
    app.register_blueprint(simplepass_blueprint)

    from .blueprints.errors import errors as errors_blueprint
    app.register_blueprint(errors_blueprint)

    return app
