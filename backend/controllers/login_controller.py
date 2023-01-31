from flask import request
from usecases.login.login_usecase import *
from usecases.login.logout_usecase import *


def login():
    data = dict(request.get_json(force=True))
    response = login_usecase(data)
    return response
   
def logout(id):
    response = logout_usecase(id)
    return response
    