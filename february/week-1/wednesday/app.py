from flask import Flask, make_response, jsonify
from frutas import Frutas

app = Flask(__name__)

@app.route('/frutas', methods=['GET'])
def get_frutas():
    return make_response(
        jsonify(Frutas)
    )

app.run()