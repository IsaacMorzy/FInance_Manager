from flask import Flask
<<<<<<< HEAD
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager



# Instance of LoginManger and using its methods

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'#monitor the changes in a user's request header and log the user out.
login_manager.login_view = 'auth.login'



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

=======
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

bootstrap = Bootstrap()
db = SQLAlchemy()

photos = UploadSet('photos', IMAGES)

def create_app(config_name):

    app = Flask(__name__)

    #Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix = '/authenticate')

    # configure UploadSet
    configure_uploads(app,photos)
    
    # Will add the views and forms

    return app
>>>>>>> d6f1d5e162ab24ff2bbae41214684f7dea3134f6
