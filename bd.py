import sqlite3


connection = sqlite3.connect("agenda_db.db")
cursor = connection.cursor()

cursor.execute("create table user (userid INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, password TEXT, status INTEGER)")


cursor.execute("create table event (eventid INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, description TEXT, date TEXT, user INTEGER)")


connection.commit()
connection.close()