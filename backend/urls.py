from database.querys import get_events, get_one_event, get_one_user, get_users, get_user_by_id
from database.inserts import insert_user, insert_event
from database.deletes import delete_event
from database.updates import update_event, update_status_user_del, update_user
from database import db  
from models.User import User
from models.Event import Event
import json
from flask import request, jsonify, Response


def urls(app):

    @app.route("/auth", methods=["POST"])
    def auth():
        body = dict(request.get_json(force=True))

        user_email = body.get("email")
        user_password = body.get("password")

        try:
            _db = db.db_connect()
            user = get_one_user(_db["cursor"], user_email, user_password)
            _db["connection"].close()

            user = {
                "id": user[0],
                "name": user[1]
            }      
            return jsonify(user), 200
        except Exception:
            return jsonify({}), 404

    # CRUD EVENT 

    @app.route("/add_event", methods=["POST"])
    def add_event():
        body = dict(request.get_json(force=True))
        event_title = body.get("title")
        event_description = body.get("description")
        event_date = body.get("date")
        user_id = body.get("user_id")

        if(event_title and event_description and event_date):
            _db = db.db_connect()
            user = insert_event(_db["cursor"], event_title, event_description, event_date, user_id)
            _db["connection"].commit()
            _db["connection"].close()
            return jsonify({}), 201
        else:
            return jsonify({}), 400

    @app.route("/event/<int:id>", methods=["GET"])
    def view_event(id):
        _db = db.db_connect()
        user = get_one_event(_db["cursor"], id)
        _db["connection"].close()
        if(user["id"]):
            return jsonify(user)
        else:
            return jsonify({}), 200

    @app.route("/list_event/<int:id>", methods=["GET"])
    def list_event(id):
        print("FEZ O GET")
        _db = db.db_connect()
        events = get_events(_db["cursor"], id)
        _db["connection"].close()

        print(events)
        if(events):
            return jsonify(events), 200
        else:
            return jsonify({}), 200


    @app.route("/edit_event/<int:id>", methods=["PUT"])
    def edit_event(id):
        body = dict(request.get_json(force=True))
        event_title = body.get("title")
        event_description = body.get("description")
        event_date = body.get("date")
        try:
            _db = db.db_connect()
            user = update_event(_db["cursor"], id, event_title, event_description, event_date)
            _db["connection"].commit()
            _db["connection"].close()
            return jsonify({}), 200
        except Exception:
            return jsonify({}), 400

    @app.route("/delete_event/<int:id>", methods=["DELETE"])
    def del_event(id):      
        try:
            _db = db.db_connect()
            event = get_one_event(_db["cursor"], id)
            delete_event(_db["cursor"], id)
            _db["connection"].commit()
            _db["connection"].close()
            return jsonify({}), 202
        except Exception:
            _db["connection"].close()
            return jsonify({}), 404


    # CRUD USER

    @app.route("/register", methods=["POST"])
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

    @app.route("/user/<int:id>",methods=["GET"])
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

    
    @app.route("/list_users", methods=["GET"])
    def list_users():
        _db = db.db_connect()
        users = get_users(_db["cursor"])
        _db["connection"].close()
        return jsonify(users), 200
    
    @app.route("/edit_user/<int:id>", methods=["PUT"])
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

    @app.route("/delete_user/<int:id>", methods=["PUT"])
    def del_user(id):
        _db = db.db_connect()
        update_status_user_del(_db["cursor"], id)
        _db["connection"].commit()
        _db["connection"].close()
        return jsonify({}), 200
        


