from flask import jsonify, request
from database.querys import *
from database.inserts import *
from database.deletes import *
from database.updates import *
from database import db  

def register():
        body = dict(request.get_json(force=True))
        print()
        user_name = body.get("name")
        user_email = body.get("email")
        user_password = body.get("password")

        if(user_name and user_email and user_password):
            _db = db.db_connect()
            user = insert_user(_db["cursor"], user_name, user_email, user_password)
            _db["connection"].commit()
            _db["connection"].close()
            return jsonify({}), 200
        else:
            return jsonify({}), 400

def view_user(id):
        _db = db.db_connect()
        print(id)
        user = get_user_by_id(_db["cursor"], id)
        _db["connection"].close()
        print("Abaixo o user: ")
        print(user)

        user = {
            "id": user[0],
            "name": user[1],
            "email": user[2]
        }

        if(len(user)):
            return jsonify(user)
        else:
            return jsonify({}), 200


def list_users():
        _db = db.db_connect()
        users = get_users(_db["cursor"])
        _db["connection"].close()
        return jsonify(users), 200

def edit_user(id):
        body = dict(request.get_json(force=True))
        print(body)
        user_name = body.get("name")
        user_email = body.get("email")
        user_password = body.get("password")
        actual_password = body.get("actual_password")

        print(actual_password)
        try:
            _db = db.db_connect()
            print(actual_password)
            user = get_user_by_id(_db["cursor"], id)
            if(user[3] != actual_password):
                _db["connection"].close()
                return jsonify({}), 400
        except Exception:
            print("ERRO 1")
            return jsonify({}), 400
        try:
            user = update_user(_db["cursor"], id, user_name, user_email, user_password)

            _db["connection"].commit()
            _db["connection"].close()
            return jsonify({}), 200
        except Exception:
            return jsonify({}), 400

def del_user(id):
        _db = db.db_connect()
        update_status_user_del(_db["cursor"], id)
        _db["connection"].commit()
        _db["connection"].close()
        return jsonify({}), 200