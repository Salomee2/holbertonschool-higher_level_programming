from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

# Cl� pour JWT (modifie-la en production)
app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)

# Utilisateurs stockés en mémoire
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """Vérifie les identifiants pour l'authentification Basic"""
    if username in users and check_password_hash(
        users[username]["password"], password
    ):
        return username
    return None


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """Route protégée par Basic Auth"""
    return jsonify({"message": "Basic Auth: Access Granted"})


@app.route("/login", methods=["POST"])
def login():
    """Endpoint de connexion pour générer un token JWT"""
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username in users and check_password_hash(
        users[username]["password"], password
    ):
        access_token = create_access_token(
            identity={"username": username, "role": users[username]["role"]}
        )
        return jsonify(access_token=access_token)

    return jsonify({"error": "Invalid credentials"}), 401


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """Route protégée par JWT"""
    return jsonify({"message": "JWT Auth: Access Granted"})


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """Route accessible uniquement aux admins"""
    current_user = get_jwt_identity()
    if current_user["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return jsonify({"message": "Admin Access: Granted"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
