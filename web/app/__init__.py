from flask import Flask
from .config import configs

def create_app(env):
    app = Flask(__name__, template_folder="../templates", static_folder="../static")
    app.config.from_object(configs[env])
    return app