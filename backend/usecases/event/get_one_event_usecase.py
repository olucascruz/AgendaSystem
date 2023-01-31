from repositories.event.event_repository import Event_repository
from flask import jsonify


def get_one_event_usecase(id):
    event_repository = Event_repository()
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