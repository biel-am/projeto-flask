/*
Exercise 1: EndPoint ping, return pong
Difficulty: Basic
Description: Create a code with an EndPoint ping that returns pong.
Expected Output: pong print.
*/

from flask import Flask

app = Flask(__name__)

@app.route('/')
def ping():
    return 'pong'

app.run()