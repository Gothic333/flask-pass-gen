import requests
import json


def generate_word(api_url, type=1):
    response = requests.get(api_url + str(type))
    data = json.loads(response.text)
    word = data['word']['word']
    return word