from flask import Flask, session
from urls import urls
from database.db import create_db
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
app.secret_key = b'kdakoaskoa_2821'


create_db()
urls(app)




if __name__ == "__main__":
    app.run(port=8000)