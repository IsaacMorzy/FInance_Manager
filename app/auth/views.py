<<<<<<< HEAD
from flask import render_template,redirect,url_for,flash,request
from ..models import User
from .forms import RegistrationForm,LoginForm
from .. import db
from flask_login import login_user,logout_user,login_required
from . import auth

@auth.route('/login')
def login():
    login_form = LoginForm()
    return render_template('auth/login.html',login_form=login_form)
=======
from flask import render_template, redirect, url_for, request,flash
from ..models import User
from .forms import RegistrationForm, LoginForm
from .. import db
from . import auth
from flask_login import login_user, logout_user, login_required

@auth.route('/login', methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user .verify_password(login_form.password.data):
            login_user(user, login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
            flash('invalid username or password')

    title = "Pitch LogIn"
    return render_template('auth/login.html', login_form = login_form, title = title)
>>>>>>> d6f1d5e162ab24ff2bbae41214684f7dea3134f6

@auth.route('/logout')
@login_required
def logout():
    logout_user()
<<<<<<< HEAD
    return redirect(url_for("main.index"))

@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.name.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
        try:
            mail_message("Welcome to Finance_Manager","email/welcome_user",user.email,user=user)
        except:
            pass
        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/register.html',registration_form= form)
=======
    return redirect(url_for('main.index'))

@auth.route('/register', methods = ["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data, password = form.password.data)

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))

    title = "New Account"
    return render_template('auth/register.html', registration_form = form)
>>>>>>> d6f1d5e162ab24ff2bbae41214684f7dea3134f6
