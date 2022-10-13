from flask import render_template, Blueprint


simplepass = Blueprint('simplepass', __name__)


@simplepass.route('/')
def index():
    return render_template('simplepass/simplepass.html', payload={})
