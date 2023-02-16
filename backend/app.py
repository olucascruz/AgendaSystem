from flask import Flask
from flask_cors import CORS
from urls import urls
from database.db import init_app

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.secret_key = b'kdakoaskoa_2821'
    init_app(app) 
    return app

app = create_app()
with app.app_context():
    urls(app)



if __name__ == "__main__":
    app.run(debug=True, port=8001)