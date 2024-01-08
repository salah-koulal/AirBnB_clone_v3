#!/usr/bin/python3
"""This module has route /status"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=["GET"])
def status():
    """return a JSON: 'status': 'OK'"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=["GET"])
def stats():
    """Return /status api route"""
    d = {
        "amenities": "Amenity",
        "cities": "City",
        "places": "Place",
        "reviews": "Review",
        "states": "State",
        "users": "User"
    }
    d = {k: storage.count(v) for k, v in d.items()}
    return jsonify(d)
