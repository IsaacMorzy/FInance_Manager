from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy



# Instance of LoginManger and using its methods

db = SQLAlchemy()


def create_app(config_name):
    '''
    Function that takes configuration setting key as an argument
    Args:
        config_name : name of the configuration to be used
    '''

    # Initialising application
    app = Flask(__name__)
    
    # Creating the app configurations
    app.config.from_object(config_options[config_name])
 


    # Initialising flask extensions

    db.init_app(app)
  

    # Registering the main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Registering the auth bluprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

  

    return app 

