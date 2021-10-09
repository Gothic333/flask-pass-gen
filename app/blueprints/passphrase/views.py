from flask import Blueprint, render_template

passphrase = Blueprint('passphrase', __name__)


@passphrase.route('/passphrase')
def index():
    return render_template('passphrase/passphrase.html', payload={})