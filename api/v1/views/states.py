#!/usr/bin/python3
"""
new view of State objects that handles all
default RESTFul API actions
"""
from models import storage
from models.state import State
from flask import jsonify, abort, request
from api.v1.views import app_views


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    """Retrieves the list of all State objects"""
    all_states = []
    states = storage.all(State).values()
    for state in states:
        all_states.append(state.to_dict())
    return jsonify(all_states)


@app_views.route('/states/<string:state_id>',
                 methods=['GET'], strict_slashes=False)
def get_state(state_id):
    """Retrieve state object"""
    all_states = []
    states = storage.all("State").values()
    for state in states:
        all_states.append(state.to_dict())
    for s in all_states:
        if s.get("id") == state_id:
            return jsonify(s)
    abort(404)


@app_views.route('/states/<string:state_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_state(state_id):
    """deletes state object"""
    states = storage.all(State)
    try:
        key = 'State.' + state_id
        storage.delete(states[key])
        storage.save()
        return jsonify({}), 200
    except BaseException:
        abort(404)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def post_state():
    """creates a new state"""
    if not request.is_json:
        abort(400, 'Not a JSON')
    else:
        request_body = request.get_json()

    if 'name' not in request_body:
        abort(400, "Missing name")
    else:
        state = State(**request_body)
        storage.new(state)
        storage.save()
        return jsonify(state.to_dict()), 201


@app_views.route("/states/<state_id>",  methods=["PUT"], strict_slashes=False)
def state_put(state_id):
    """
    updates specific State object by ID
    :param state_id: state object ID
    :return: state object and 200 on success, or 400 or 404 on failure
    """
    state_json = request.get_json(silent=True)
    if state_json is None:
        abort(400, 'Not a JSON')
    fetched_obj = storage.get("State", str(state_id))
    if fetched_obj is None:
        abort(404)
    for key, val in state_json.items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(fetched_obj, key, val)
    fetched_obj.save()
    return jsonify(fetched_obj.to_json())
