from flask import Flask
from flask_cors import CORS
from urls import urls
from database.db import db_connect

app = Flask(__name__)
CORS(app)
app.secret_key = b'kdakoaskoa_2821'
db_connect()
urls(app)




if __name__ == "__main__":
    app.run(debug=True, port=8001)