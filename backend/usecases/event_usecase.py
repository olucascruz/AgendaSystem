from datetime import datetime
from flask import jsonify
class EventUsecase:
    def __init__(self, repository) -> None:
        self.repository = repository


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
                event_repository = EventRepository()
                event_repository.create_event(event_title, event_description, event_date, user_id)
                return jsonify({'message': 'event created'}), 201
            except Exception:
                return jsonify({'message': 'error add'}), 400    
        else:
            return jsonify({'message': 'event need title and date'}), 400

    def get_all_event_user_usecase(id):
        event_repository = EventRepository()
        try:
            all_events = event_repository.real_all_events_user(id)
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
            
            return jsonify(events)
        except Exception:
            return jsonify({'message':'not exist events'})



    def get_one_event_usecase(id):
        event_repository = EventRepository()
        data_event = event_repository.read_one_event(id)

        try:
            date_and_hour = data_event[3].split()
            date = date_and_hour[0]
            hour = date_and_hour[1]
            event = {
                "id": data_event[0],
                "title": data_event[1],
                "description": data_event[2],
                "date": date,
                "hour": hour,
                }

            return jsonify(event)
        except Exception:
            return jsonify({'message':'event not exist'})

    def edit_event_usecase(id, data):
        event_title = data.get("title")
        event_description = data.get("description")
        event_date = data.get("date")
        event_hour = data.get("hour")
        event_repository = EventRepository()

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


    def del_event_usecase(id):
        event_repository = EventRepository()
        try:
            event_repository.del_user(id)
            return jsonify({"message":"event deleted"}), 202
        except Exception:
            return jsonify({"message":"error delete event "}), 400