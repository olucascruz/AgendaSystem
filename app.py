import sqlite3
import random
from flask import Flask, session, render_template, request, g, redirect, url_for
from flask_session import Session
from datetime import datetime


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'




@app.route("/")
def index():
    users = get_users()
    return render_template("login.html", users = users)

@app.route("/calendar")
def calendar():
    if session["name"] == None:
        return redirect(url_for("login"))
    return render_template("calendar.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/register_user", methods=["post"])
def register_user():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect("agenda_db.db")
        cursor = db.cursor()
        
        user_name = request.form["name"]
        user_email = request.form["email"]
        user_password = request.form["password"]
        cursor.execute("insert into user (name, email, password, status) values (?,?,?,?)", [user_name, user_email, user_password, 0])
    
    db.commit()
    return redirect(url_for("calendar"))

def get_users():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect("agenda_db.db")
        cursor = db.cursor()
        cursor.execute("select * from user")
        all_users = cursor.fetchall()
        all_users = [str(val) for val in all_users]
    print(all_users)
    return all_users

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        db = getattr(g, "_database", None)
        if db is None:
            db = g._database = sqlite3.connect("agenda_db.db")
            cursor = db.cursor()
            user_email = request.form["email"]
            user_password = request.form["password"]
            cursor.execute(f'select * from user where email = ? and password = ?', (user_email, user_password))
            data_login = cursor.fetchone()
            
            print(data_login)
            
            session["id"] = data_login[0]
            session["name"] = data_login[1]
            session["email"] = data_login[2]

        return redirect(url_for("calendar"))
    else:
        return render_template('login.html')

@app.route("/add_event", methods=["GET", "POST"])
def add_event():
    if request.method == "POST":
        db = getattr(g, "_database", None)
        if db is None:
            db = g._database = sqlite3.connect("agenda_db.db")
            cursor = db.cursor()
            
            event_title = request.form["title"]
            event_description = request.form["description"]
            event_date = request.form["date"]
            event_hour =  request.form["hour"]

            if not event_title:
                event_title = "Meu evento"

            
            date_string = event_date+" "+event_hour
            
            event_complete_date = datetime.strptime(date_string, '%Y-%m-%d %H:%M').strftime('%d/%m/%y %H:%M')
            cursor.execute("insert into event (title, description, date, user) values (?,?,?,?)", [event_title, event_description, event_complete_date, session["id"]])
        
        db.commit()
        return redirect(url_for("list_event"))
    else: 
        return render_template("addEvent.html")

@app.route('/logout')
def logout():
    session["id"] = None
    session["name"] = None
    session["email"] = None
    return redirect(url_for('login'))


def get_events():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect("agenda_db.db")
        cursor = db.cursor()
        cursor.execute("select * from event where user = ?", [session["id"]])
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



@app.route("/list_event")
def list_event():
    if session["name"] == None:
        return redirect(url_for("login"))
    events = get_events()
    session["events"] = events
    return render_template("listEvents.html", events = events)

@app.route("/event/<int:id>")
def view_event(id):
    a_event = get_one_event(id)
    return render_template("event.html", event=a_event)

@app.route("/del_event", methods=["post"])
def del_event():
    id_event = request.form["id"]   
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect("agenda_db.db")
        cursor = db.cursor()
        cursor.execute(f'delete from event where eventid = ?', [id_event])
    db.commit()
    return redirect(url_for("list_event"))



@app.route("/edit_event/<int:id>", methods=["get", "post"])
def edit_event(id):
    if request.method == "POST":
        db = getattr(g, "_database", None)
        if db is None:
            db = g._database = sqlite3.connect("agenda_db.db")
            cursor = db.cursor()
            title_event = request.form["title"]
            description_event = request.form["description"]
            date_event = request.form["date"]
            hour_event = request.form["hour"]

            date_complete = date_event + " " + hour_event 
            try:
                cursor.execute(f'update event set title = ?, description = ?, date = ? where eventid = ?', [title_event, description_event, date_complete, id])
            except Exception as ex:
                print(ex)
        db.commit()
        return redirect(url_for("list_event"))
    
    a_event = get_one_event(id)
    return render_template("/editEvent.html", event=a_event)

@app.route("/user")
def view_user():
    render_template("user.html")

def get_one_event(id):
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect("agenda_db.db")
        cursor = db.cursor()
        cursor.execute(f'select * from event where eventid = ?', [id])
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

def get_one_user():
        user ={
            "id":  session["id"], 
            "name": session["name"], 
            "email":session["email"]
        } 

        return user
@app.teardown_appcontext
def close_connection(exeption):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()
    

if __name__ == "__main__":
    app.run()