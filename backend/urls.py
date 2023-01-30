from database.querys import *
from database.inserts import *
from database.deletes import *
from database.updates import *
from controllers.login_controller import *
from controllers.event_controller import *
from controllers.user_controller import *


def urls(app):

    app.add_url_rule("/login",
    "login", login, methods=["POST"])
    app.add_url_rule("/logout/<int:id>",
    "logout", logout)

    # CRUD EVENT 

    app.add_url_rule("/add_event",
    "add_event", add_event, methods=["POST"])
    
    app.add_url_rule("/event/<int:id>",
    "get_event", get_event)
    
    app.add_url_rule("/list_event/<int:id>", "list_events", list_events)

    app.add_url_rule("/edit_event/<int:id>", "edit_event", edit_event, methods=["PUT"])
    
    app.add_url_rule("/delete_event/<int:id>", "del_event", del_event, methods=["DELETE"])
    
    
    # CRUD USER
    app.add_url_rule("/register",
    "register", register, methods=["POST"])
    
    app.add_url_rule("/user/<int:id>",
    "view_user", view_user)
   
    app.add_url_rule("/list_users",
    "list_users", list_users)
    
    app.add_url_rule("/edit_user/<int:id>",
    "edit_user", edit_user, methods=["PUT"])

    app.add_url_rule("/delete_user/<int:id>",
    "del_user", del_user, methods=["PUT"])
