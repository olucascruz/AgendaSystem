from repositories.event.event_repository import Event_repository
from datetime import datetime
from flask import jsonify



def edit_event_usecase(id, data):
    event_title = data.get("title")
    event_description = data.get("description")
    event_date = data.get("date")
    event_hour = data.get("hour")
    event_repository = Event_repository()

    if not event_title:
            event_title = "Meu evento"

    if len(event_date) > 0 and len(event_hour) > 0:    
        date_string = event_date+" "+event_hour
        
        event_date = datetime.strptime(date_string, '%Y-%m-%d %H:%M').strftime('%d/%m/%y %H:%M')


    try:
        
        event_repository.edit_event(id, event_title, event_description, event_date)
        
        return jsonify({'message':'event edited'}), 200
    except Exception:
        return jsonify({'message':'error edit event'}), 400