from flask import Flask, session
from urls import urls
from database.db import create_db, db_connect
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
app.secret_key = b'kdakoaskoa_2821'


db_connect()
urls(app)




if __name__ == "__main__":
    app.run(debug=True, port=8001)