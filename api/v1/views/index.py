#!/usr/bin/python3
"""
launches a Flask web application.
"""
from flask import jsonify
from models import storage
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def status():
    """Show the status response."""
    return jsonify(status="OK")


@app_views.route('/stats', strict_slashes=False)
# This code has the advantage of not returning non-existing objects
def stats():
    """display type-specific object counts"""
    all_classes = {"Amenity": "amenities", "City": "cities", "Place": "places",
                   "Review": "reviews", "State": "states", "User": "users"}
    return jsonify({v: storage.count(k) for k, v in all_classes.items()
                    if storage.count(k)})
