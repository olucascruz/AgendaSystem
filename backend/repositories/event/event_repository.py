from database.db import db_connect  

class Event_repository:
    def __init__(self) -> None:
        self.db = db_connect()

    def create_event(self, event_title, event_description, event_date, user_id):
        self.db['cursor'].execute("INSERT INTO event (title, description, date, user) VALUES (?,?,?,?)", [event_title, event_description, event_date, user_id])
        self.db['connection'].commit()

        return True

    def read_one_event(self, id):
        self.db['cursor'].execute(f'SELECT * FROM event WHERE eventid = ?', [id])
        data_event = self.db['cursor'].fetchone()
        
        
        return data_event
    
    def real_all_events_user(self, user_id):
        self.db['cursor'].execute("SELECT * FROM event WHERE user = ?", [user_id])
        all_events = self.db['cursor'].fetchall()

        return all_events

    def edit_event(self, id, title, description, date):
        self.db['cursor'].execute(f'UPDATE event SET title = ?, description = ?, date = ? WHERE eventid = ?', [title, description, date, id])
        self.db['connection'].commit()

    def del_user(self, id_event):    
        self.db['cursor'].execute(f'DELETE FROM event WHERE eventid = ?', [id_event])
        self.db['connection'].commit()

