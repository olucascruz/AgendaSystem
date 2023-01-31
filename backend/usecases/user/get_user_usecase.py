from repositories.user.user_repository import User_repository
from flask import jsonify

def get_user_usecase(id):
    user_respository = User_repository()
    try:
        user = user_respository.get_user_by_id(id)
        user = {
            "id": user[0],
            "name": user[1],
            "email": user[2]
        }
        return jsonify(user), 200
    except Exception:
        return jsonify({"message":"error get user"}), 400
