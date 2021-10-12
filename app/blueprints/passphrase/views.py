from flask import Blueprint, render_template
from .utils import generate_word

passphrase = Blueprint('passphrase', __name__)


@passphrase.route('/passphrase')
def index():
    return render_template('passphrase/passphrase.html', payload={})


@passphrase.route('/passphrase/api/<int:word_number>', methods=['GET', 'POST'])
def parseWords(word_number):
    words = []
    api_url = 'http://free-generator.ru/generator.php?action=word&type='
    if word_number == 1:
        words.append(generate_word(api_url, type=1))
    else:
        word_type = 2
        for i in range(word_number):
            word = generate_word(api_url, type=word_type)
            words.append(word)
            if not word_type - 1:
                word_type = 3
            else:
                 word_type -= 1
    data = {'phrase': " ".join(words).capitalize()}
    return data