from flask import render_template, request, redirect, url_for, session
import requests
from api import api_request
from datetime import datetime
import requests
import json

API = api_request()



def index():
        try:
           users = API.get_users()

        except Exception:
            users = "falha de conexão"
        print(users)
        return render_template("login.html", users = users)

def register_user():
        if request.method == "POST":
            
            data = dict(request.form)
            API.register(data)

            return redirect(url_for("login"))
        else:
            return render_template("register.html")

def login():
        if request.method == "POST":

            data = dict(request.form)            
            response = requests.post(API+'login', json.dumps(data))

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

def logout():
        requests.put(API+"list_event/"+str(session["user_id"]))
        session.clear()
        return redirect(url_for('login'))

def calendar():
        if session["name"] == None:
            return redirect(url_for("login"))
        events = requests.get(API+"list_event/"+str(session["user_id"]))
        events = list(events.json())
        return render_template("calendar.html", events=events)

def list_event():
        if session["name"] == None:
            return redirect(url_for("login"))
        print("AQUI É O USER ID: ",session["user_id"])
        events = requests.get(API+"list_event/"+str(session["user_id"]))
        events = list(events.json())
        return render_template("listEvents.html", events = events)


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

def view_event(id):
        event = requests.get(API+"event/"+str(id))
        event = dict(event.json())
        return render_template("event.html", event=event)

def del_event():
        id_event = request.form["id"]   
        event = requests.delete(API+"delete_event/"+id_event)
        return redirect(url_for("list_event"))

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

def view_user():
        print("user id: ", session["user_id"])
        user = requests.get(API+"user/"+str(session["user_id"]))
        user = dict(user.json())
        print(user)
        return render_template("user.html", user = user)


def edit_user():
        if request.method == "POST":
            data = dict(request.form)
            response =  requests.put(API+"edit_user/"+str(session["user_id"]), json.dumps(data))
            
            if(response.status_code == 200):
                return redirect(url_for("view_user"))
            
            error = "Senha incorreta"
            return render_template("edit_user.html", error=error)
        return render_template("edit_user.html")


def del_user():
        if request.method == "POST":
            data = dict(request.form)

            delete = requests.put(API+"delete_user/"+str(session["user_id"]), json.dumps(data))
            
            return redirect(url_for("login"))