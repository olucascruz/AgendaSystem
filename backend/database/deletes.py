def delete_event(cursor, id_event):
    cursor.execute(f'delete from event where eventid = ?', [id_event])

    