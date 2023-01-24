def delete_event(cursor, id_event):
    cursor.execute(f'DELETE FROM event WHERE eventid = ?', [id_event])

    