from views import * 



def routes(app):


    # LOGIN
    app.add_url_rule("/",
    "index", index)
    
    app.add_url_rule("/register_user",
    "register_user", register_user, methods=["GET","POST"])
    
    app.add_url_rule("/login",
    "login", login, methods=["GET","POST"])
    
    app.add_url_rule("/logout",
    "logout", logout)
    
    # ENTER APP
    app.add_url_rule("/calendar",
    "calendar", calendar)
    
    app.add_url_rule("/list_event",
    "list_event", list_event)

    # CRUD EVENT
    app.add_url_rule("/add_event",
    "add_event", add_event, methods=["GET", "POST"])
    
    app.add_url_rule("/event/<int:id>",
    "view_event", view_event)
    
    app.add_url_rule("/del_event",
    "del_event", del_event, methods=["POST"])

    app.add_url_rule("/edit_event/<int:id>",
    "edit_event", edit_event, methods=["GET", "POST"])
    
    
    # CRUD USER
    app.add_url_rule("/user",
    "view_user", view_user)
    
    app.add_url_rule("/edit_user",
    "edit_user", edit_user, methods=["GET", "POST"])
    
    app.add_url_rule("/del_user",
    "del_user", del_user, methods=["POST"])