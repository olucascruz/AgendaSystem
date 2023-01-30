from flask import jsonify, request
from database.querys import *
from database.inserts import *
from database.deletes import *
from database.updates import *
from database import db  
from datetime import datetime

def add_event():
        body = dict(request.get_json(force=True))
        event_title = body.get("title")
        event_description = body.get("description")
        event_date = body.get("date")
        event_hour = body.get("hour")
        user_id = body.get("user_id")

        if not event_title:
            event_title = "Meu evento"

        
        date_string = event_date+" "+event_hour
        
        event_date = datetime.strptime(date_string, '%Y-%m-%d %H:%M').strftime('%d/%m/%y %H:%M')


        if(len(event_title) != 0 and len(event_date) != 0):
            _db = db.db_connect()
            insert_event(_db["cursor"], event_title, event_description, event_date, user_id)
            _db["connection"].commit()
            _db["connection"].close()
            return jsonify({'message': 'event created'}), 201
        else:
            return jsonify({}), 400


def get_event(id):
        _db = db.db_connect()
        event = get_one_event(_db["cursor"], id)
        _db["connection"].close()
        if "id" in event:
            return jsonify(event)
        else:
            return jsonify({}), 200

def list_events(id):
        print(id)
        print("FEZ O GET")
        _db = db.db_connect()
        events = get_events(_db["cursor"], id)
        _db["connection"].close()

        print(events)
        if(events):
            return jsonify(events), 200
        else:
            return jsonify({}), 200

def edit_event(id):
    if request.method == "PUT":
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
    else:
        return jsonify({}), 400

def del_event(id):
        if request.method == "DELETE":      
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
        return jsonify({}), 404