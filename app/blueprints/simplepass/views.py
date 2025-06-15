from flask import Blueprint, render_template

simplepass = Blueprint('simplepass', __name__)


@simplepass.route('/')
def index():
    return render_template('simplepass/simplepass.html')
