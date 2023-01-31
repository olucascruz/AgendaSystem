from repositories.user.user_repository import User_repository
from flask import jsonify


def logout_usecase(id):
    user_repository = User_repository()
    try:
        user_repository.update_status_user_desactive(id)
        return jsonify({"message: logout"}), 200
    
    except Exception:
        return jsonify({"message: error"}), 400
