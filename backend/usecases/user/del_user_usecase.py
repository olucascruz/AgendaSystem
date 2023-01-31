from repositories.user.user_repository import User_repository
from flask import jsonify


def del_user_usecase(id):
    user = User_repository()
    try:
        user.update_status_user_del(id)
    except Exception:
        return jsonify({"message":"error delete user"})