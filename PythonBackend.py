import json
from flask import Flask, jsonify, request # import objects from the Flask model
import requests


app = Flask(__name__) # define app using Flask


@app.route('/', methods=['GET'])
def returnAll():
    url = 'https://swapi.co/api/starships/?format=json'
    response = requests.get(url)
    text = response.json()

    text["results"] = [dict(starships=ele["films"]) for ele in text["results"]]

    jsonData = json.dumps(text)
    resp = json.loads(jsonData)
    with open('text.json', 'w') as fp:
        json.dump(resp, fp, indent=4, sort_keys=True)

    return resp['results'][0]


if __name__ == '__main__':
    app.run(debug=True, port=8080)
