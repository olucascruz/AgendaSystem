import sqlite3
import random
from flask_cors import CORS
from flask import Flask, session
from flask_session import Session
from routes import routes

def run_app():
    app = Flask(__name__)
    CORS(app)
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    
    routes(app, session)
    app.run(debug=True, port=5001)

if __name__ == "__main__":
    run_app()