from flask import Flask, session, render_template, request, g, redirect, url_for, jsonify
from backend.database import db, db_close
from backend.database.querys import get_events, get_one_event, get_one_user, get_users
import sqlite3
from datetime import datetime
from backend.database.inserts import insert_user, insert_event
import requests


def routes(app, session):
    @app.route("/")
    def index():
        users = dict(requests.get('http://127.0.0.1:5000/list_users'))
        return render_template("login.html", users = users)

    @app.route("/calendar")
    def calendar():
        if session["name"] == None:
            return redirect(url_for("login"))
        return render_template("calendar.html")

        
    @app.route("/register_user", methods=["GET","POST"])
    def register_user():
        if request.method == "POST":
                
            user_name = request.form["name"]
            user_email = request.form["email"]
            user_password = request.form["password"]
            _db = db.db_connect()
            insert_user(_db.cursor, user_name, user_email, user_password)
            _db["connection"].close()
            
            db.commit()
            return redirect(url_for("calendar"))
        else:
            return render_template("register.html")

    

    @app.route("/login", methods=["GET","POST"])
    def login():
        if request.method == "POST":
            user_email = request.form["email"]
            user_password = request.form["password"]
            data={
                "email":user_email,
                "password":user_password
            }
            user = dict(requests.post('http://127.0.0.1:5000/auth', jsonify(data)))

            print(user)
            session["name"]=user[1]
            session["user_id"]=user[0]
            

            if(user):
                return redirect(url_for("calendar"))
            else:
                return render_template('login.html')
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
                _db = db.db_connect()
                insert_event(_db["cursor"], event_title, event_description, event_complete_date, session["user_id"])
                _db["connection"].commit()
                _db["connection"].close()
    
            
            db.commit()
            return redirect(url_for("list_event"))
        else: 
            return render_template("addEvent.html")

    @app.route('/logout')
    def logout():
        session.clear()
        return redirect(url_for('login'))






    @app.route("/list_event")
    def list_event():
        if session["name"] == None:
            return redirect(url_for("login"))
        _db = db.db_connect()
        events = get_events(_db["cursor"], session["user_id"])
        _db["connection"].close()
    
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
        _db = db.db_connect()
        a_event = get_one_event(_db["cursor"],id)
        _db["connection"].close()
        
        return render_template("/editEvent.html", event=a_event)

    @app.route("/user")
    def view_user():
        render_template("user.html")
