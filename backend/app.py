from flask import Flask
from flask_cors import CORS
from flask_session import Session   # Add this import
from utils.db import init_db
from routes.products import bp as products_bp
from routes.auth import bp as auth_bp

def create_app():
    app = Flask(__name__)
    app.secret_key = 'secretkey123'  # For session mgmt

    # Add server-side session config
    app.config['SESSION_TYPE'] = 'filesystem'
    Session(app)  # Initialize server-side session support

    # Enable CORS with credentials support
    CORS(app, supports_credentials=True)

    init_db(app)
    app.register_blueprint(products_bp)
    app.register_blueprint(auth_bp)
    return app

if __name__ == '__main__':
    create_app().run(debug=True)
