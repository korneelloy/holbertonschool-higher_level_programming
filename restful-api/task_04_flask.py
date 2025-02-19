#!/usr/bin/python3

"""Flask test module"""

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route('/')
def home():
    """ function to handle ('/) route. returns the view."""
    return "Welcome to the Flask API!"


@app.route('/data')
def data():
    """ function to handle ('/data) route. returns the view."""
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """ function to handle ('/status) route. returns the view."""
    return "OK"


@app.route('/users/<username>')
def users(username):
    """ function to handle ('/users/<username>') route. returns the view """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """ function to handle ('/add_user') route. returns the view."""
    new_user = request.get_json()
    username = new_user.get("username")
    if not username:
        return jsonify('{"error": "Username is required"}'), 400
    else:
        return jsonify({"message": "User added", "user": new_user}), 201


if __name__ == "__main__":
    app.run()
