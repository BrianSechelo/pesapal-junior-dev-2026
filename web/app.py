from flask import Flask, request, jsonify
from db.database import Database
from db.engine import Engine

app = Flask(__name__)

# Create database + engine (in-memory)
db = Database("web_db")
engine = Engine(db)

# Create users table on startup
engine.execute(
    "CREATE TABLE users (id INT PRIMARY KEY, email TEXT UNIQUE, name TEXT)"
)


@app.route("/users", methods=["POST"])
def create_user():
    data = request.json

    command = (
        f"INSERT INTO users VALUES ({data['id']}, "
        f"'{data['email']}', '{data['name']}')"
    )

    result = engine.execute(command)
    return jsonify({"message": result}), 201


@app.route("/users", methods=["GET"])
def list_users():
    result = engine.execute("SELECT * FROM users")
    return jsonify(result), 200


if __name__ == "__main__":
    app.run(debug=True)
