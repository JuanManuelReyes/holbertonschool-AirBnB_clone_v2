#!/usr/bin/python3
"""
Write a script that starts a Flask web application.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_HBNB():
    """
    Display Hello HBNB!
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """
    Display HBNB
    """
    return 'HBNB'

@app.route("/c/<text>", strict_slashes=False)
def print_C(text):
    """
    display “C ” followed by the value of the text variable
    (replace underscore _ symbols with a space).
    """
    final_text = text.replace("_", " ")
    return f"C {final_text}"

if __name__ == '__main__':
    """
    listening on 0.0.0.0, port 5000
    """
    app.run(host="0.0.0.0", port="5000")