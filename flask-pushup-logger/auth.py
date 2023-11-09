from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('/register')
def register():
    return 'Register page'


@auth.route('/login')
def login():
    return 'Login page'


@auth.route('/logout')
def logout():
    return 'Logout page'
