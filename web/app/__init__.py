from flask import Flask
from .config import configs
from .database import db
from .redis import r


def create_app(env):
    app = Flask(__name__, template_folder="../templates", static_folder="../static")
    app.config.from_object(configs[env])

    db.init_app(app)
    if app.config["REDIS_ENABLED"]:
        r.init_app(app)

    from .main import main_bp

    app.register_blueprint(main_bp)

    from .teams import teams_bp

    app.register_blueprint(teams_bp)

    return app
