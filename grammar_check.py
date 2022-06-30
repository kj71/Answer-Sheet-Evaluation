import requests

api_key = "Cot8T3kBauUx7GMG"


def check(text):
    params = {
        'text': text,
        'key': api_key
    }

    response = requests.get(url="https://api.textgears.com/grammar", params=params)
    num_errors = len(response.json()['response']['errors'])
    return num_errors

