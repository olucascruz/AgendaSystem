from database.db import get_db  


class UserRepository:
    def __init__(self) -> None:
        self.db = get_db()
        self.cursor = self.db.cursor()

    def get_users(self):
        self.cursor.execute("SELECT * from user")
        all_users = self.cursor.fetchall()
        all_users = [tuple(row) for row in all_users]
        return all_users

    def register(self, user_name, user_email, user_password):
        self.cursor.execute("insert into user (name, email, password, status) values (?,?,?,?)", [user_name, user_email, user_password, 0])
        self.db.commit()

    def auth_db(self, user_email, user_password):
        try:    
            self.cursor.execute(f'SELECT * FROM user WHERE email = ? AND password = ?', [user_email, user_password])
            user = self.cursor.fetchone()
            return user
        except Exception as e:
            print(e)

    def update_status_user_active(self, id):   
        self.cursor.execute('UPDATE user SET status = ? WHERE userid = ?', [1, id])
        self.db.commit()
    
        return True

    def update_status_user_desactive(self, id):   
        self.cursor.execute('UPDATE user SET status = ? WHERE userid = ?', [0, id])
        self.db.commit()
    
        return True

    def get_user_by_id(self, id):
        self.cursor.execute(f'SELECT * FROM user WHERE userid = ?', [id])
        user = self.cursor.fetchone()

        return user

    def update_user(self, id, name, email, password):
        self.cursor.execute(f'UPDATE user SET name = ?, email = ?, password = ? WHERE userid = ?', [name, email, password, id])
        self.db.commit()

    def update_status_user_del(self, id):
        self.cursor.execute(f'UPDATE user SET status = ? WHERE userid = ?', [-1, id])
        self.db.commit()
        
    