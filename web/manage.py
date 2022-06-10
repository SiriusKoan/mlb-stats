from os import getenv
from app import create_app
from app.database.helper import db_initialization

app = create_app(getenv("FLASK_ENV") or "development")


@app.shell_context_processor
def make_shell_context():
    return globals()


@app.cli.command(name="init_db")
def init_db():
    db_initialization()
