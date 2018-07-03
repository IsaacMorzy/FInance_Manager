import os

class Config:

  
    SQLALCHEMY_DATABASE_URI= 'postgresql+psycopg2://isaac:morzy@localhost/finance' #location of the database with authentication.
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}