import sqlite3
def create_db():
    db = "agenda_db.db"
    connection = sqlite3.connect(db)
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS user  (userid INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, password TEXT, status INTEGER)")


    cursor.execute("CREATE TABLE IF NOT EXISTS event (eventid INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, description TEXT, date TEXT, user INTEGER)")

    cursor.execute("insert into user (name, email, password, status) values (?,?,?,?)", ["Lucas", "Lucas", "Lucas", 0])
    connection.commit()
    connection.close()