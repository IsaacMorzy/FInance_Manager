
from .import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

class User(db.Model):#class that will help us create new users then pass in db.model as an argument.This connects the class to the database and allow communication
   
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



