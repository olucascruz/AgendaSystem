from flask import jsonify, request
from database.querys import *
from database.inserts import *
from database.updates import *
from usecases.user.register_user_usecase import *
from usecases.user.get_user_usecase import *
from usecases.user.edit_user_usecase import *
from usecases.user.del_user_usecase import *




from database import db  
 
def register():
        data = dict(request.get_json(force=True))
        response = register_user_usecase(data)
        return response
        
def view_user(id):
        response = get_user_usecase(id)
        return response

def list_users():
        _db = db.db_connect()
        users = get_users(_db["cursor"])
        _db["connection"].close()
        return jsonify(users), 200

def edit_user(id):
        data = dict(request.get_json(force=True))
        response = edit_user_usecase(id, data)
        return response
        

def del_user(id):
    response = del_user_usecase(id)
    return response