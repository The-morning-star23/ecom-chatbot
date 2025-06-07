from flask import Blueprint, request, jsonify, session
from utils.db import mysql
import bcrypt

bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    print(f"Login attempt: username={username} password={password}")

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT id, password_hash FROM users WHERE username=%s", (username,))
    user = cursor.fetchone()
    print(f"User fetched from DB: {user}")

    if user:
        stored_hash = user[1]
        print(f"Stored hash: {stored_hash}")
        # bcrypt requires bytes, stored hash is str in DB, so encode both correctly
        if bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8')):
            session['user_id'] = user[0]
            print(f"Login successful for user_id {user[0]}")
            return jsonify({"message": "Login successful"})
        else:
            print("Password mismatch")
    else:
        print("User not found")

    return jsonify({"error": "Invalid credentials"}), 401

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode('utf-8')

    cursor = mysql.connection.cursor()
    try:
        cursor.execute("INSERT INTO users(username, password_hash) VALUES (%s, %s)", (username, hashed))
        mysql.connection.commit()
        return jsonify({"message": "Registered successfully"})
    except Exception as e:
        print("Register error:", e)
        return jsonify({"error": "Username already exists"}), 400
