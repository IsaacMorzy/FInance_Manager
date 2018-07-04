
from app import create_app,db
from flask_script import Manager,Server
from app.models import User
from flask_migrate import Migrate,MigrateCommand


# Creating app instance
app = create_app('development')

manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command('server',Server)
manager.add_command('db',MigrateCommand)

@manager.command
def test():
    '''
    Run the unit tests
    '''

from app import create_app, db
from flask_script import Manager, Server
from app.models import User
from flask_migrate import Migrate, MigrateCommand

app = create_app('development')

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('server',Server)
manager.add_command('db', MigrateCommand)

manager.add_command('server',Server)
@manager.command
def test():
    """Run the unit tests."""

    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.shell # Flask script allows us to create a Python shell inside our application. It will be useful to test features in our app and for debugging.
def make_shell_context():
    return dict(app = app,db = db,User = User)#returns app applicaton instance .db database instance ,User 

if __name__ == '__main__':
    manager.run()


    

@mana.shell
def make_shell_context():
    return dict(app = app,db = db,User = User)

if __name__ == '__main__':
    manager.run()

