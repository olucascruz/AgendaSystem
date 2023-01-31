from database.db import db_connect  


class User_repository:
    def __init__(self) -> None:
        self.db = db_connect()

    def register(self, user_name, user_email, user_password):
        self.db['cursor'].execute("insert into user (name, email, password, status) values (?,?,?,?)", [user_name, user_email, user_password, 0])
        self.db['connection'].commit()

    def auth_db(self, user_email, user_password):    
        self.db['cursor'].execute(f'SELECT * FROM user WHERE email = ? AND password = ?', [user_email, user_password])
        user = self.db['cursor'].fetchone()
        return user

    def update_status_user_active(self, id):   
        self.db['cursor'].execute('UPDATE user SET status = ? WHERE userid = ?', [1, id])
        self.db['connection'].commit()
    
        return True

    def update_status_user_desactive(self, id):   
        self.db['cursor'].execute('UPDATE user SET status = ? WHERE userid = ?', [0, id])
        self.db['connection'].commit()
    
        return True

    def get_user_by_id(self, id):
        self.db['cursor'].execute(f'SELECT * FROM user WHERE userid = ?', [id])
        user = self.db['cursor'].fetchone()
    
        return user

    def update_user(cursor, id, name, email, password):
        cursor.execute(f'UPDATE user SET name = ?, email = ?, password = ? WHERE userid = ?', [name, email, password, id])

    def update_status_user_del(cursor, id):
        cursor.execute(f'UPDATE user SET status = ? WHERE userid = ?', [-1, id])
        
    