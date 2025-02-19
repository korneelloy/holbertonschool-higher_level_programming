#!/usr/bin/python3

"""
Develop a Simple API using Python with Flask
"""

from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_jwt_extended import get_jwt_identity


app = Flask(__name__)

auth = HTTPBasicAuth()

app.config["JWT_SECRET_KEY"] = "klsq87!/xcjk<yyu65"

jwt = JWTManager(app)


users = {}

"""BASIC PROTECTION"""


@auth.verify_password
def verify_password(username, password):
    """password check with simple verification"""
    if username in users and\
       check_password_hash(users[username]["password"], password):
        return username


@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    """view returning with basic protection"""
    return ("Basic Auth: Access Granted")


"""TOKEN PROTECTION"""


@app.route('/login', methods=['POST'])
def login():
    """password check with JWT / token"""
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username in users and\
       check_password_hash(users[username]["password"], password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)

    return jsonify({"message": "Invalid credentials"}), 401


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """view returning with jwt protection"""
    return jsonify({"message": "JWT Auth: Access Granted"})


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    """view returning with jwt protection for admin"""
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return jsonify({"message": "Admin Access: Granted"})


if __name__ == '__main__':
    app.run()
