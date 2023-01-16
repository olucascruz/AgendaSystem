import sqlite3
import random
from flask import Flask, session, render_template, request, g, redirect, url_for
from flask_session import Session
from datetime import datetime
from routes import routes
from database.db import db_connect 

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

db_connect()


routes(app, session)



# @app.teardown_appcontext
# def close_connection(exeption):
#     db = getattr(g, "_database", None)
#     if db is not None:
#         db.close()
    

if __name__ == "__main__":
    app.run()