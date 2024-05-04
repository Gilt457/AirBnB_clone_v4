#!/usr/bin/python3
"""
state object view for all RestFul API defaults
"""
from flask import jsonify, abort, request
from models import storage
from api.v1.views import app_views
from models.state import State


@app_views.route('/states', methods=['GET', 'POST'], strict_slashes=False)
def handle_states():
    """Returns all State objects or creates a new one."""
    if request.method == 'GET':
        return jsonify([obj.to_dict() for obj in storage.all("State").
                        values()]), 200
    if request.method == 'POST':
            if not request.get_json(silent=True):
                abort(400, "Not a JSON")
            if not request.get_json(silent=True).get('name'):
                abort(400, "Missing name")
            kwargs = request.get_json(silent=True)
            new_state = State(**kwargs)
            new_state.save()
            return jsonify(new_state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['GET', 'DELETE', 'PUT'],
                 strict_slashes=False)
def state_byid(state_id):
    """Retrieves, deletes, or updates State objects by id."""
    state_obj = storage.get("State", state_id)
    if state_obj:
        if request.method == 'GET':
            return jsonify(state_obj.to_dict()), 200
        elif request.method == 'DELETE':
            storage.delete(state_obj)
            storage.save()
            return {}, 200
        elif request.method == 'PUT':
            if not request.get_json(silent=True):
                abort(400, "Not a JSON")
            kwargs = request.get_json(silent=True)
            if kwargs:
                for key, value in kwargs.items():
                    if key not in ["id", "created_at", "updated_at"]:
                        setattr(state_obj, key, value)
                state_obj.save()
            return jsonify(state_obj.to_dict()), 200
    else:
        # When the state_id is not linked to any State object
        abort(404)
