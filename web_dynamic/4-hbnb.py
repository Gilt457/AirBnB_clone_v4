#!/usr/bin/python3
""" Initialize a Flask Web Application """
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
from flask import Flask, render_template
import uuid

app = Flask(__name__)


# Configure Jinja environment to remove leading spaces and newline characters

@app.teardown_appcontext
def close_db(error):
    """ Terminate the current database session """
    storage.close()


@app.route('/4-hbnb/', strict_slashes=False)
def hbnb():
    """ Confirm that the HBNB application is operational """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []

    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)

    return render_template('0-hbnb.html',
                           states=st_ct,
                           amenities=amenities,
                           places=places,
                           cache_id=uuid.uuid4())


if __name__ == "__main__":
    """ Execute the main driver function """
    app.run(host='0.0.0.0', port=5001)
