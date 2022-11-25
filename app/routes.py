#from crypt import methods
from flask import render_template, redirect, flash, url_for
from app import app
from app.forms import LoginForm
from flask_login import login_user
from app.models import User

@app.route('/')
@app.route('/index')
def index():
    #return "Hello, World"
    user_info = {'city': 'Hue', 'name': 'Thanh'}
    title = ''
    number_list = ['one', 'two', 'three']
    return render_template('index.html', user = user_info, title=title, list=number_list)

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        flash(f"Username: {login_form.username.data}")
        user = User.query.filter(User.username==login_form.username.data).first()
        if user is None or not User.check_password(login_form.password):
            flash(f"Invalid username")
            return redirect(url_for('login'))
        login_user(user)
        return redirect('index')
    return render_template('login.html', form=login_form)