from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('/register')
def register_page():
    return render_template('register.html')


@auth.route('/login')
def login_page():
    return render_template('login.html')


@auth.route('/logout')
def logout_page():
    return 'Logout page'
