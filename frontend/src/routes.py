from flask import Flask, session, render_template, request, g, redirect, url_for, jsonify
import sqlite3
from datetime import datetime
import requests
import json

API = 'http://127.0.0.1:8000/'
def routes(app, session):

    # LOGIN
    @app.route("/")
    def index():
        try:
            users = requests.get(API+'list_users')
            users = users.text
        except Exception:
            users = "falha de conexão"
        print(users)
        return render_template("login.html", users = users)
     
    @app.route("/register_user", methods=["GET","POST"])
    def register_user():
        if request.method == "POST":
                
            user_name = request.form["name"]
            user_email = request.form["email"]
            user_password = request.form["password"]
            data ={
                "name":user_name,
                "email":user_email,
                "password":user_password
            }
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
            
            response = requests.post(API+'auth', json.dumps(data))

            body = dict(response.json())
            if(response.status_code == 200): 
                session["user_id"]=body["id"]
                session["name"]= body["name"]

                return redirect(url_for("calendar"))
            else:
                error = "Dados invalidos"
                return render_template('login.html', error = error)
        else:
            return render_template('login.html')

    @app.route('/logout')
    def logout():
        session.clear()
        return redirect(url_for('login'))

    # ENTER APP
    @app.route("/calendar")
    def calendar():
        if session["name"] == None:
            return redirect(url_for("login"))
        return render_template("calendar.html")
   
    @app.route("/list_event")
    def list_event():
        if session["name"] == None:
            return redirect(url_for("login"))
        print("AQUI É O USER ID: ",session["user_id"])
        events = requests.get(API+"list_event/"+str(session["user_id"]))
        events = list(events.json())
        return render_template("listEvents.html", events = events)

    # CRUD EVENT
    @app.route("/add_event", methods=["GET", "POST"])
    def add_event():
        if request.method == "POST":
            event_title = request.form["title"]
            event_description = request.form["description"]
            event_date = request.form["date"]
            event_hour =  request.form["hour"]

            if not event_title:
                event_title = "Meu evento"

            
            date_string = event_date+" "+event_hour
            
            event_complete_date = datetime.strptime(date_string, '%Y-%m-%d %H:%M').strftime('%d/%m/%y %H:%M')
           
            data = {
                "title":event_title,
                "description":event_description,
                "date":event_complete_date,
                "user_id":session["user_id"]
            }

            event = requests.post(API+"add_event", json.dumps(data))

            return redirect(url_for("list_event"))
        else: 
            return render_template("addEvent.html")

    @app.route("/event/<int:id>")
    def view_event(id):
        event = requests.get(API+"event/"+str(id))
        event = dict(event.json())
        return render_template("event.html", event=event)

    @app.route("/del_event", methods=["POST"])
    def del_event():
        id_event = request.form["id"]   
        event = requests.delete(API+"delete_event/"+id_event)
        return redirect(url_for("list_event"))

    @app.route("/edit_event/<int:id>", methods=["GET", "POST"])
    def edit_event(id):
        if request.method == "POST":
            title_event = request.form["title"]
            description_event = request.form["description"]
            date_event = request.form["date"]
            hour_event = request.form["hour"]

            date_complete = date_event + " " + hour_event 
            
            if not title_event:
                title_event = "Meu evento"

            data = {
                "title":title_event,
                "description":description_event,
                "date":date_complete 
            }
            
            response = requests.put(API+"edit_event/"+str(id), json.dumps(data))

          
            if(response.status_code == 200):
                return redirect(url_for("list_event"))
            else:
                print("error ao editar")
                return redirect(url_for("list_event"))
        
        event = requests.get(API+"event/"+str(id))
        event = dict(event.json())
        return render_template("editEvent.html", event=event)


    # CRUD USER
    @app.route("/user", methods=["GET"])
    def view_user():
        print("user id: ", session["user_id"])
        user = requests.get(API+"user/"+str(session["user_id"]))
        user = dict(user.json())
        print(user)
        return render_template("user.html", user = user)

    @app.route("/edit_user", methods=["GET", "POST"])
    def edit_user():
        if request.method == "POST":
            print(request.form)
            name = request.form["name"]
            email = request.form["email"]
            password = request.form["password"]
            actual_password = request.form["actual_password"]


            data = {
                "name":name,
                "email":email,
                "password":password,
                "actual_password": actual_password
            }

            print("AAAAAAAAA")
            response =  requests.put(API+"edit_user/"+str(session["user_id"]), json.dumps(data))
            
            if(response.status_code == 200):
                return redirect(url_for("view_user"))
            
            error = "Senha incorreta"
            return render_template("edit_user.html", error=error)
        return render_template("edit_user.html")
    
    @app.route("/del_user", methods=["POST"])
    def del_user():
        if request.method == "POST":
            password = request.form["password"]

            data = {
                "password": password
            }

            delete = requests.put(API+"delete_user/"+str(session["user_id"], jsonify(data)))

            if delete:
                return redirect(url_for("logout"))
            
            error = "Senha incorreta"
            return redirect(url_for("user", error))