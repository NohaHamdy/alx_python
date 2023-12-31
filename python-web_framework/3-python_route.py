#!/usr/bin/python3
""" Four routes  """
from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def task_0():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def task_1():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def task_2(text):
    word = text.split('_')
    return f"C {' '.join(word)}"

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def task_3(text='is cool'):
    word = text.split('_')

    return f"Python {' '.join(word)}"

if __name__ == "__main__":
    app.run(debug=True)