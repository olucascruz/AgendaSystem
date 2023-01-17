def insert_user(cursor, user_name, user_email, user_password):
     cursor.execute("insert into user (name, email, password, status) values (?,?,?,?)", [user_name, user_email, user_password, 0])


def insert_event(cursor, event_title, event_description, event_date, id):
     cursor.execute("INSERT INTO event (title, description, date, user) VALUES (?,?,?,?)", [event_title, event_description, event_date, id])