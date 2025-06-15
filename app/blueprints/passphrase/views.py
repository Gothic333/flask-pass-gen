import json
import os

import requests
from flask import Blueprint, current_app, jsonify, render_template

passphrase = Blueprint('passphrase', __name__)


@passphrase.route('/')
def index():
    return render_template('passphrase/passphrase.html')


@passphrase.route('/api/<int:word_number>', methods=['GET', 'POST'])
def parse_words(word_number):
    api_url = current_app.config.get('PHRASE_API_URL')
    words = []
    word_type = 1 if word_number == 1 else 2

    for _ in range(word_number):
        params = {'action': 'word', 'type': word_type}
        response = requests.get(api_url, params=params)
        try:
            response.raise_for_status()
            data = json.loads(response.text)

            word = data.get('word', {}).get('word')
            words.append(word)

            word_type -= 1
            if not word_type:
                word_type = 3
        except requests.HTTPError:
            return jsonify({"error": "Phrase generator internal error"}), 500

                
    return jsonify({'phrase': " ".join(words).capitalize()})
