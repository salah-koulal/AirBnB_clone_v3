#!/usr/bin/python3
"""This module has route /status"""
from models import storage
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from flask import Flask, jsonify
from api.v1.views import app_views


amenities_ = storage.count(Amenity)
cities_ = storage.count(City)
places_ = storage.count(Place)
reviews_ = storage.count(Review)
states_ = storage.count(State)
users_ = storage.count(User)


data = {"amenities": amenities_,
        "cities": cities_,
        "places": places_,
        "reviews": reviews_,
        "states": states_,
        "users": users_
        }


@app_views.route('/status', methods=["GET"])
def status():
    """return a JSON: 'status': 'OK'"""
    resp = jsonify({"status": "OK"})
    resp.status_code = 200
    return resp


@app_views.route('/stats')
def stats():
    """Retrieves the number of each objects by type"""
    return jsonify(data)
