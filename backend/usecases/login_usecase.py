from flask import jsonify

class LoginUsecase:
    def __init__(self, repository) -> None:            
        self.user_repository = repository

    def login(self, data):
        # print(self.user_repository.auth_db)
        user_email = data.get("email")
        user_password = data.get("password")
        try:
            print(user_email)
            user = self.user_repository.auth_db(user_email, user_password)
            if user[3] != -1:
                self.user_repository.update_status_user_active(user[0])
                
                user = {
                    "id": user[0],
                    "name": user[1]
                }      
                return jsonify(user), 200
            else: 
                return jsonify({}), 404
        except Exception:
            return jsonify({}), 404

    def logout(self, id):
        try:
            self.user_repository.update_status_user_desactive(id)
            return jsonify({"message":"logout"}), 200
        
        except Exception:
            return jsonify({"message": "error"}), 400