from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options


bootstrap = Bootstrap()

def create_app(config_name):

    # create app instance
    app = Flask(__name__)

    # create app configurationks 
    app.config.from_object(config_options[config_name])

    # initialize flask extension 
    bootstrap.init_app(app)

    # register blue print
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .request import configure_request
    configure_request(app)

    return app