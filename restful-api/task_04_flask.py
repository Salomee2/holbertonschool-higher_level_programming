#!/usr/bin/python3
"""Simple Flask API"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
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


@app.route('/', methods=['GET'])
def home():
    """Root endpoint"""
    return "Welcome to the Flask API!\n"


@app.route('/status', methods=['GET'])
def status():
    """Health check endpoint"""
    return "OK"


@app.route('/data', methods=['GET'])
def get_usernames():
    """Returns a list of all usernames"""
    return jsonify(list(users.keys()))


@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    """Returns user data for a given username"""
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route('/add_user', methods=['POST'])
def add_user():
    """Adds a new user to the API"""
    data = request.get_json()

    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
