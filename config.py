import os

class Config:
    CSRF_INSTALLED = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI', 'postgresql+psycopg2://murungi:murungi1@localhost/plog')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY="svcdsdhgcvghsg"

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI', 'postgresql+psycopg2://murungi:murungi1@localhost/plog')
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    }