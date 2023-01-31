from flask import render_template, request, redirect, url_for
import requests
from api import api_request
import requests

API = api_request()



def index():
        try:
           users = API.get_users()

        except Exception:
            users = "falha de conexão"
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
            is_logged = API.login(data)

            
            if(is_logged): 

                return redirect(url_for("calendar"))
            else:
                error = "Dados invalidos"
                return render_template('login.html', error = error)
        else:
            return render_template('login.html')

def logout():
        API.logout()
        return redirect(url_for('login'))

def calendar():
        if not API.is_logged:
            return redirect(url_for("login"))
        events = API.get_events()
        return render_template("calendar.html", events=events)

def list_event():
        if not API.is_logged:
            return redirect(url_for("login"))
        events = API.get_events()
        return render_template("listEvents.html", events = events)


def add_event(): 
    context = {
        "add_event": API.add_event(),
        "user_id": API.user_id
    }
    return render_template("addEvent.html", context=context)

def view_event(id):
        event = API.get_event(str(id))
        return render_template("event.html", event=event)

def del_event():
        id_event = request.form["id"]
        response = API.delete_event(id_event)
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
            
            response = API.edit_event(str(id), data)
          
            if(response.status_code == 200):
                return redirect(url_for("list_event"))
            else:
                return redirect(url_for("list_event"))
        
        event = API.get_event(str(id))
        return render_template("editEvent.html", event=event)

def view_user():
        user = API.get_user()
        return render_template("user.html", user = user)


def edit_user():
        if request.method == "POST":
            data = dict(request.form)
            response = API.edit_user(data)
            
            
            if(response.status_code == 200):
                return redirect(url_for("view_user"))
            
            error = "Senha incorreta"
            return render_template("edit_user.html", error=error)
        return render_template("edit_user.html")


def del_user():
        if request.method == "POST":
            data = dict(request.form)

            API.delete_user()
            
            return redirect(url_for("login"))