from flask import Flask, request, jsonify
from flask_cors import CORS
from crud import create_user, get_users, update_user, delete_user

app = Flask(__name__)
CORS(app)


# CREATE
@app.route("/users", methods=["POST"])
def add_user():
    try:
        data = request.json

        if not data or "name" not in data or "age" not in data:
            return jsonify({"error": "Name and age are required"}), 400

        create_user(data["name"], data["age"])
        return jsonify({"message": "User created"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# READ
@app.route("/users", methods=["GET"])
def fetch_users():
    users = get_users()
    return jsonify(users)

# UPDATE
@app.route("/users/<int:user_id>", methods=["PUT"])
def edit_user(user_id):
    try:
        data = request.json

        if not data or "name" not in data or "age" not in data:
            return jsonify({"error": "Name and age are required"}), 400

        update_user(user_id, data["name"], data["age"])
        return jsonify({"message": "User updated"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# DELETE
@app.route("/users/<int:user_id>", methods=["DELETE"])
def remove_user(user_id):
    try:
        delete_user(user_id)
        return jsonify({"message": "User deleted"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)