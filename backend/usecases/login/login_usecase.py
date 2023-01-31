from repositories.user.user_repository import User_repository
from flask import jsonify

def login_usecase(data):
    user_email = data.get("email")
    user_password = data.get("password")
    
    user_repository = User_repository()
    try:
        user = user_repository.auth_db(user_email, user_password)
        if user[3] != -1:
            user_repository.update_status_user_active(user[0])
             
            user = {
                "id": user[0],
                "name": user[1]
            }      
            return jsonify(user), 200
        else: 
            return jsonify({}), 404
    except Exception:
        return jsonify({}), 404

        