#!/usr/bin/python3
"""This module has route /status"""
from api.v1.views import app_views
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


@app_views.route('/status', methods=["GET"], strict_slashes=False)
def status():
    """return a JSON: 'status': 'OK'"""
    return {
        "status": "OK",
    }


@app_views.route('/stats', methods=["GET"], strict_slashes=False)
def stats():
    """Return /status api route"""
    return {
        "amenities": storage.count(Amenity),
        "cities": storage.count(City),
        "places": storage.count(Place),
        "reviews": storage.count(Review),
        "states": storage.count(State),
        "users": storage.count(User),
    }
