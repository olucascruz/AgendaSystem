import sqlite3

def get_events(cursor, user_id):

    cursor.execute("SELECT * FROM event WHERE user = ?", [user_id])
    all_events = cursor.fetchall()

    events = []

    for event in all_events:
        date_and_hour = event[3].split()
        date = date_and_hour[0]
        hour = date_and_hour[1]
        a_event = {
            "id": event[0],
            "title": event[1],
            "description": event[2],
            "date": date,
            "hour": hour,
        }
        events.append(a_event)

    return events

def get_one_event(cursor, id):
    cursor.execute(f'SELECT * FROM event WHERE eventid = ?', [id])
    data_event = cursor.fetchone()
    
    date_and_hour = data_event[3].split()
    date = date_and_hour[0]
    hour = date_and_hour[1]
    a_event = {
        "id": data_event[0],
        "title": data_event[1],
        "description": data_event[2],
        "date": date,
        "hour": hour,
        }
    return a_event

def get_one_user(cursor, user_email, user_password):    
    cursor.execute(f'SELECT * FROM user WHERE email = ? AND password = ?', (user_email, user_password))
    user = cursor.fetchone()
    
    return user
    


def get_users(cursor):    
    cursor.execute("SELECT * from user")
    all_users = cursor.fetchall()
    all_users = [str(val) for val in all_users]
    print(all_users)
    return all_users