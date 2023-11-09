from flask import Blueprint, render_template

main = Blueprint('main', __name__)


@main.route('/')
def home_page():
    return 'Home page'


@main.route('/profile')
def profile_page():
    return 'Profile page'
