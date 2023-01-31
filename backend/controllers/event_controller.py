from flask import jsonify, request
from database.querys import *
from database.inserts import *
from database.deletes import *
from database.updates import *
from database.db import db_connect  
from usecases.event.add_event_usecase import *
from usecases.event.get_one_event_usecase import *
from usecases.event.get_all_event_user_usecase import *
from usecases.event.edit_event_usecase import *
from usecases.event.del_event_usecase import *





def add_event():
        data = dict(request.get_json(force=True))
        response = add_event_usecase(data)
        return response


def get_event(id):
    response = get_one_event_usecase(id)
    return response
        

def list_events(id):
        response = get_all_event_user_usecase(id)
        return response

def edit_event(id):
    data = dict(request.get_json(force=True))
    response = edit_event_usecase(id, data)
    return response


def del_event(id):
        response = del_event_usecase(id)
        return response    
            