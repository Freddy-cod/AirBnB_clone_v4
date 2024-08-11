#!/usr/bin/python3
"""
Flask App
"""
from flask import Flask, render_template, url_for
from models import storage
import uuid


# Set flast
app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'


# Start rendering
@app.teardown_appcontext
def teardown_db(exception):
    """
    Remove
    """
    storage.close()


@app.route('/1-hbnb/')
def hbnb_filters(the_id=None):
    """
    Custom templates
    """
    state_objs = storage.all('State').values()
    states = dict([state.name, state] for state in state_objs)
    amens = storage.all('Amenity').values()
    places = storage.all('Place').values()
    users = dict([user.id, "{} {}".format(user.first_name, user.last_name)]
                 for user in storage.all('User').values())
    return render_template('1-hbnb.html',
                           states=states,
                           amens=amens,
                           places=places,
                           users=users, cache_id=uuid.uuid4())

if __name__ == "__main__":
    """
    App-Main"""
    app.run(host=host, port=port)
