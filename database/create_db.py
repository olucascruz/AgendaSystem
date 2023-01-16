import sqlite3
def create_db():
    db = "agenda2_db.db"
    connection = sqlite3.connect(db)
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE user (userid INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, password TEXT, status INTEGER)")


    cursor.execute("CREATE TABLE event (eventid INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, description TEXT, date TEXT, user INTEGER)")

    connection.commit()
    connection.close()