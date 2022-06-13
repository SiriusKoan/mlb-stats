from os import getenv, urandom

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Testing(Config):
    # Flask
    ENV = "TESTING"
    TESTING = True
    SECRET_KEY = "93249yn5g4m5n"
    SERVER_NAME = "localhost"
    # Flask-SQLAlchemy
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    # Flask-WTF
    WTF_CSRF_ENABLED = False

class Development(Config):
    # Flask
    ENV = "DEVELOPMENT"
    DEBUG = True
    SECRET_KEY = "93249yn5g4m5n"
    # Flask-SQLAlchemy
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"

class Production(Config):
    # Flask
    ENV = "PRODUCTION"
    SECRET_KEY = urandom(32)
    # Flask-SQLAlchemy
    SQLALCHEMY_DATABASE_URI = getenv("DATABASE_URI")

configs = {
    "development": Development,
    "testing": Testing,
    "production": Production,
}