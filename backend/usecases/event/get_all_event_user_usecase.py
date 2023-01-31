from repositories.event.event_repository import Event_repository
from flask import jsonify

def get_all_event_user_usecase(id):
    event_repository = Event_repository()
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