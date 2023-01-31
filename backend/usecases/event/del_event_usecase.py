from repositories.event.event_repository import Event_repository
from flask import jsonify

def del_event_usecase(id):
    event_repository = Event_repository()
    try:
        event_repository.del_user(id)
        return jsonify({"message":"event deleted"}), 202
    except Exception:
        return jsonify({"message":"error delete event "}), 400