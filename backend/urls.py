from database.querys import get_events, get_one_event, get_one_user, get_users
from database.inserts import insert_user, insert_event
from database.deletes import delete_event
from database import db  
from models.User import User
from models.Event import Event


import json
from flask import request, jsonify, Response


def urls(app):

    @app.route("/auth", methods=["POST"])
    def auth():
        body = dict(request.json)
        print()
        user_email = body.get("email")
        user_password = body.get("password")

        _db = db.db_connect()
        user = get_one_user(_db["cursor"], user_email, user_password)
        _db["connection"].close()
        if(user):      
            return jsonify(user)
        else:
            return jsonify({}), 404

    @app.route("/event/<int:id>", methods=["GET"])
    def view_event(id):
        _db = db.db_connect()
        user = get_one_event(_db["cursor"], id)
        _db["connection"].close()
        if(user):
            return jsonify(user)
        else:
            return jsonify({}), 200

    @app.route("/list_event", methods=["GET"])
    def list_event():
        _db = db.db_connect()
        id = 0
        events = get_events(_db["cursor"], id)
        _db["connection"].close()
        if(events):
            return jsonify(events)
        else:
            return jsonify({}), 200

    @app.route("/list_users", methods=["GET"])
    def list_users():
        _db = db.db_connect()
        users = get_users(_db["cursor"])
        _db["connection"].close()
        return jsonify(users), 200

    @app.route("/register", methods=["POST"])
    def register():
        body = dict(request.json)
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
        
    @app.route("/add_event", methods=["POST"])
    def add_event():
        body = dict(request.json)
        event_title = body.get("title")
        event_description = body.get("description")
        event_date = body.get("date")

        if(event_title and event_description and event_date):
            _db = db.db_connect()
            user = insert_event(_db["cursor"], event_title, event_description, event_date)
            _db["connection"].commit()
            _db["connection"].close()
            return jsonify({}), 201
        else:
            return jsonify({}), 400

    @app.route("/edit_event/<int:id>", methods=["PUT"])
    def edit_event():
        body = dict(request.json)
        event_title = body.get("title")
        event_description = body.get("description")
        event_date = body.get("date")

        if(event_title and event_description and event_date):
            _db = db.db_connect()
            user = insert_event(_db["cursor"], event_title, event_description, event_date)
            _db["connection"].commit()
            _db["connection"].close()
            return jsonify({}), 201
        else:
            return jsonify({}), 400

    @app.route("/edit_user/<int:id>", methods=["PUT"])
    def edit_user():
        pass

    @app.route("/delete_event/<int:id>", methods=["DELETE"])
    def del_event(id):
        _db = db.db_connect()
        event = get_one_event(_db["cursor"])
        if(event):
            delete_event(_db["cursor"], id)
            _db["connection"].commit()
            _db["connection"].close()
            return jsonify({}), 202
        else:
            _db["connection"].close()
            return jsonify({}), 404

    @app.route("/delete_user/<int:id>", methods=["DELETE"])
    def del_user():
        pass



