from flask import render_template,redirect,url_for,flash,request
from ..models import User
from .forms import RegistrationForm,LoginForm
from .. import db
from flask_login import login_user,logout_user,login_required
from . import auth
@auth.route('/login')
def login():
    login_form = LoginForm()
    return render_template('auth/login.html'login_form=login_form)