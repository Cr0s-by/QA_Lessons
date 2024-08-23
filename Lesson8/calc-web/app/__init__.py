from flask import Flask

from configuration import Config


def create_application(config):
    new_app = Flask(__name__)
    new_app.config.from_object(config)

    return new_app


application = create_application(Config)
import app.routes.routes

