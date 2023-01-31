from flask import Flask, session
from flask_session import Session
from routes import routes


app = Flask(__name__)   
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

routes(app)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
