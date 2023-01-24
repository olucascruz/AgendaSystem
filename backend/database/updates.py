def update_event(cursor, id, title, description, date):
    cursor.execute(f'UPDATE event SET title = ?, description = ?, date = ? WHERE eventid = ?', [title, description, date, id])



def update_status_user_del(cursor, id):
    cursor.execute(f'UPDATE user SET status = ? WHERE userid = ?', [-1, id])

def update_status_user_desactive(cursor, id):
    cursor.execute(f'UPDATE user SET status = ? WHERE userid = ?', [0, id])

def update_status_user_active(cursor, id):
    cursor.execute(f'UPDATE user SET status = ? WHERE userid = ?', [1, id])

def update_user(cursor, id, name, email, password):
    cursor.execute(f'UPDATE user SET name = ?, email = ?, password = ? WHERE userid = ?', [name, email, password, id])