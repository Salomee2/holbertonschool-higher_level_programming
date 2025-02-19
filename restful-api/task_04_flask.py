from flask import Flask, jsonify, request

app = Flask(__name__)

# Initialiser un dictionnaire pour stocker les utilisateurs
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

# Route d'accueil
@app.route('/')
def home():
    return "Bienvenue sur l'API Flask !"

# Route pour obtenir tous les utilisateurs
@app.route('/data')
def get_users():
    return jsonify(list(users.keys()))

# Route pour vérifier l'état de l'API
@app.route('/status')
def status():
    return "OK"

# Route pour obtenir un utilisateur par son nom d'utilisateur
@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "Utilisateur introuvable"}), 404

# Route pour ajouter un utilisateur
@app.route('/add_user', methods=['POST'])
def add_user():
    user_data = request.get_json()

    # Vérifier que le nom d'utilisateur est présent
    if 'username' not in user_data:
        return jsonify({"error": "Le nom d'utilisateur est requis"}), 400

    username = user_data['username']

    # Ajouter l'utilisateur dans le dictionnaire
    users[username] = {
        "username": username,
        "name": user_data.get("name"),
        "age": user_data.get("age"),
        "city": user_data.get("city")
    }

    return jsonify({
        "message": "Utilisateur ajouté",
        "user": users[username]
    }), 201

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)
