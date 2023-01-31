from repositories.user.user_repository import User_repository
from flask import jsonify

def edit_user_usecase(id, data):
    user_name = data.get("name")
    user_email = data.get("email")
    user_password = data.get("password")
    actual_password = data.get("actual_password")

    user_repository = User_repository()
    try:
        user = user_repository.get_user_by_id(id)
        if(user[3] != actual_password):
            return jsonify({}), 400
    except Exception:
        return jsonify({}), 400
    try:
        user = user_repository.update_user(id, user_name, user_email, user_password)

        return jsonify(user), 200
    except Exception:
        return jsonify({}), 400