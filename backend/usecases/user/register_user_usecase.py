from repositories.user.user_repository import User_repository
from flask import jsonify


def register_user_usecase(data):
    user_repository = User_repository()
    user_name = data.get("name")
    user_email = data.get("email")
    user_password = data.get("password")

    
    if(user_name and user_email and user_password):
        user_repository.register(user_email, user_email, user_password)
        return jsonify({}), 200
    else:
        return jsonify({}), 400