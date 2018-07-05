
from .import db
from werkzeug.security import generate_password_hash,check_password_hash
from .import login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    '''
    @login_manager.user_loader Passes in a user_id to this function
    Function queries the database and gets a user's id as a response
    '''
    return User.query.get(int(user_id))
class User(UserMixin,db.Model):#class that will help us create new users then pass in db.model as an argument.This connects the class to the database and allow communication
   
    __tablename__ = 'users'#allows us to give the tables in our database proper names
   
    id = db.Column(db.Integer,primary_key = True)#specifies the data in the column to be integer
    username = db.Column(db.String(255))#db.String specifies the data in the column should be a string with a max of 255 characters
    email = db.Column(db.String(255),unique=True,index=True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))

    @property # creates a write only class property password.
    def password(self):
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
            self.pass_secure = generate_password_hash(password)
            #generate a password hash and pass the hashed password as a value to the pass_secure column property to save to the database.


    def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)
        
   

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'User {self.username}'
        #makes it easier to debug our apps

class Budget(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.relationship('Category', backref='budget', uselist=False)
    limit = db.Column(db.Integer)

    def __repr__(self):
        return '<Budget for {}>'.format(self.category)


class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    description = db.Column(db.String(160))
    cost = db.Column(db.Integer)
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Purchase {}>'.format(self.description)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_text = db.Column(db.String(120), unique=True)
    expenses = db.relationship('Expense', backref='category', lazy='dynamic')
    budget_id = db.Column(db.Integer, db.ForeignKey('budget.id'))

    def __repr__(self):
        return '{}'.format(self.category_text.title())

