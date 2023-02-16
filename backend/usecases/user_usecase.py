from flask import jsonify


class UserUsecase:
    def __init__(self, repository) -> None:
        self.repository = repository


    def register_user_usecase(data):
        user_repository = UserRepository()
        user_name = data.get("name")
        user_email = data.get("email")
        user_password = data.get("password")

        
        if(user_name and user_email and user_password):
            user_repository.register(user_email, user_email, user_password)
            return jsonify({}), 200
        else:
            return jsonify({}), 400

    def get_user_usecase(id):
        user_respository = UserRepository()
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

    def edit_user_usecase(id, data):
        user_name = data.get("name")
        user_email = data.get("email")
        user_password = data.get("password")
        actual_password = data.get("actual_password")
        
        print(actual_password)
        user_repository = UserRepository()

        user = user_repository.get_user_by_id(id)
        

        if(user[3] == actual_password):    
            try:
                user = user_repository.update_user(id, user_name, user_email, user_password)

                return jsonify(user), 200
            except Exception:
                return jsonify({"message":"error password"}), 400
        return jsonify({"message":"error update"}), 400


    def del_user_usecase(id):
        user = UserRepository()
        try:
            user.update_status_user_del(id)
        except Exception:
            return jsonify({"message":"error delete user"})