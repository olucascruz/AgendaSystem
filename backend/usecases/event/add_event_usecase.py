from datetime import datetime
from repositories.event.event_repository import Event_repository
from flask import jsonify

def add_event_usecase(data):
        event_title = data.get("title")
        event_description = data.get("description")
        event_date = data.get("date")
        event_hour = data.get("hour")
        user_id = data.get("user_id")

        if not event_title:
            event_title = "Meu evento"

        
        date_string = event_date+" "+event_hour
        
        event_date = datetime.strptime(date_string, '%Y-%m-%d %H:%M').strftime('%d/%m/%y %H:%M')

        if(len(event_title) != 0 and len(event_date) != 0):
            try:
                event_repository = Event_repository()
                event_repository.create_event(event_title, event_description, event_date, user_id)
                return jsonify({'message': 'event created'}), 201
            except Exception:
                return jsonify({'message': 'error add'}), 400    
        else:
            return jsonify({'message': 'event need title and date'}), 400