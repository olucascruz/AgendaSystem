from flask import jsonify, request
from database.querys import *
from database.inserts import *
from database.deletes import *
from database.updates import *
from database import db  

def login():
    if request.method == "POST":
        body = dict(request.get_json(force=True))

        user_email = body.get("email")
        user_password = body.get("password")
        print(user_email)
        try:
            _db = db.db_connect()
            user = auth_db(_db["cursor"], user_email, user_password)
            _db["connection"].close()

            user = {
                "id": user[0],
                "name": user[1]
            }      
            return jsonify(user), 200
        except Exception:
            return jsonify({}), 404
    else:
        return jsonify({}), 404


def logout(id):
    _db = db.db_connect()
    user = update_status_user_desactive(_db["cursor"], id)
    _db["connection"].close()
    