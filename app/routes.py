#from crypt import methods
from flask import render_template, redirect, flash, url_for,  request 
from app import app
from app.forms import LoginForm, RegisterForm
from flask_login import login_required, login_user, current_user, logout_user
from app.models import User
from werkzeug.urls import url_parse
from app import db
@app.route('/')
@app.route('/index')
@login_required
def index():
    user = current_user
    posts = user.posts
    #return "Hello, World"
    return render_template('index.html', user = user, posts = posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if not current_user.is_anonymous:
        flash(f"you have already logged in")
        return redirect('index')
    login_form = LoginForm()
    if login_form.validate_on_submit():
        flash(f"Username: {login_form.username.data}")
        user = User.query.filter(User.username==login_form.username.data).first()
        if user is None or not user.check_password(login_form.password.data):
            flash(f"Invalid username")
            return redirect(url_for('login'))
        login_user(user) 
        flash(f'you have logged in successfully')
        next_page = request.args.get('next')
        if next_page is None or url_parse(next_page).netloc:
            next_page = 'index'
        return redirect(next_page)
    return render_template('login.html', form=login_form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    reg_form =RegisterForm()
    if reg_form.validate_on_submit():
        name = reg_form.username.data
        password = reg_form.password.data
        #kiem tra da co trong bang User hay chua
        user = User(username = name, password = password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
        
    return render_template('register.html', form = reg_form)