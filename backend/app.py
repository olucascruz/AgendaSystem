from flask import Flask
from urls import urls
from database.db import create_db, db_connect

app = Flask(__name__)
app.secret_key = b'kdakoaskoa_2821'


db_connect()
urls(app)




if __name__ == "__main__":
    app.run(debug=True, port=8001)