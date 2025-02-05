"""
Exercise 3: People informations
Difficulty: Basic
Description: Create a code to return people informations
Expected Output: All people data
"""

from flask import Flask, make_response, jsonify
from pessoas import Pessoas

app = Flask(__name__)

@app.route('/pessoas', methods=['GET'])
def get_pessoas():
    return make_response(
        jsonify(Pessoas)
    )

app.run()