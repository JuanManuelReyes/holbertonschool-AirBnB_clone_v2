#!/usr/bin/python3
"""
Write a script that starts a Flask web application.
"""

from flask import Flask, render_template
from models import storage
from models.state import State

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
    return "C {}".format(final_text)


"""
With strict slashes /python and /python/ have the same result
"""


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def print_py(text='is cool'):
    """
    display “Python ”, followed by the value of the text
    variable (replace underscore _ symbols with a space )
    """
    final_text = text.replace("_", " ")
    return "Python {}".format(final_text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    display “n is a number” only if n is an integer
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    display a HTML page only if n is an integer
    h1 tag: “Number: n” inside the tag body
    """
    return render_template('5-number.html', number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even_template(n):
    """
    display a HTML page only if n is an integer
    H1 tag: “Number: n is even|odd” inside the tag BODY
    """
    if (n % 2) == 0:
        desc = "even"
    else:
        desc = "odd"
    return render_template("6-number_odd_or_even.html", number=n,
                           desc=desc)


@app.teardown_appcontext
def teardown(self):
    """
    remove the current SQLAlchemy Session
    """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def stateslist():
    """
    display a HTML page: (inside the tag BODY)
    H1 tag: “States”
    UL tag: with the list of all State objects
    present in DBStorage sorted by name (A->Z)
    LI tag: description of one State: <state.id>: <B><state.name></B>
    """
    all_states = storage.all(State).values()
    return render_template("7-states_list.html", all_states=all_states)


if __name__ == '__main__':
    """
    listening on 0.0.0.0, port 5000
    """
    app.run(host="0.0.0.0", port="5000")
