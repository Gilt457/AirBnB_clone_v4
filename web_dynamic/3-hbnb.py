#!/usr/bin/python3
""" Initiates a Flask Web Application """
# Importing necessary models and Flask components
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
from flask import Flask, render_template
import uuid

app = Flask(__name__)


# Configurations for Jinja environment to remove unnecessary spaces
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True

# Function to execute when the application context ends
@app.teardown_appcontext
def close_db(error):
    """ Closes the current SQLAlchemy Session """
    storage.close()


# Defines the route for the HBNB page
@app.route('/3-hbnb/', strict_slashes=False)
def hbnb():
    """ Confirms that the HBNB service is operational """
    # Retrieve and sort states from the database
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []

    # Organize states and their cities
    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

    # Retrieve and sort amenities and places from the database
    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)

    # Render the template with the sorted data and a unique cache identifier
    return render_template('0-hbnb.html',
                           states=st_ct,
                           amenities=amenities,
                           places=places,
                           cache_id=uuid.uuid4())


# Entry point for running the Flask application
if __name__ == "__main__":
    """ Executes the Flask application """
    app.run(host='0.0.0.0', port=5001)
