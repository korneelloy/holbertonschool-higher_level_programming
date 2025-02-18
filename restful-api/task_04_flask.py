from flask import Flask, jsonify, request

"""Flask test module"""
app = Flask(__name__)

users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
        },
    "john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
        }
       }


@app.route('/')
def home():
    # function to handle ('/) route. returns the view.
    return "Welcome to the Flask API!", 200


@app.route('/data/')
def returnUsers():
    # function to handle ('/data) route. returns the view.
    names = [user["username"] for user in users.values()]
    return jsonify(names), 200


@app.route('/status/')
def returnStatus():
    # function to handle ('/status) route. returns the view.
    return jsonify({"status": "OK"}), 200


@app.route('/users/<username>')
def returnUser(username):
    # function to handle ('/users/<username>') route. returns the view.
    if username in users:
        return jsonify(users[username]), 200
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user/', methods=['POST'])
def addUser():
    # function to handle ('/add_user') route. returns the view.
    new_user = request.get_json()
    if new_user is not None:
        username = new_user.get('username')
        if username:
            users[username] = new_user
            return jsonify({"message": "User added", "user": new_user}), 201
        else:
            return jsonify('{"error": "Username is required"}'), 400
    else:
        return ("Something went wrong", 400)


if __name__ == "__main__":
    app.run()
