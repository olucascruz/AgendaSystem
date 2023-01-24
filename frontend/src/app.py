import sqlite3
import random
from flask_cors import CORS
from flask import Flask, session
from flask_session import Session
from datetime import datetime
from routes import routes

app = Flask(__name__)
CORS(app)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


routes(app, session)



# @app.teardown_appcontext
# def close_connection(exeption):
#     db = getattr(g, "_database", None)
#     if db is not None:
#         db.close()
    

if __name__ == "__main__":
    app.run(debug=True, port=5001)