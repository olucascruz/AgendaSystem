import requests
import json

class api_request():
    def __init__(self) -> None:
        self.BASE_URL = 'http://127.0.0.1:8000/'
        self.user_id = ''
        self.is_logged = False
    
    def __set_user_id(self, user_id):
        self.user_id = user_id
    
    def __set_is_logged(self, bool):
        self.is_logged = bool

    def get_is_logged(self):
        return self.is_logged

    def login(self):
        response = requests.post(self.BASE_URL+'login')
        if response.status_code == 200: 
            body = dict(response.json())
            self.__set_user_id(body["id"])
            self.__set_is_logged(True)
            return True
        
        return False            
         
    
    def get_user(self) -> dict:
        endpoint = 'user/'

        response = requests.get(self.BASE_URL+endpoint+ self.user_id)

        user = dict(response.json())
        return user

    def get_users(self):
        endpoint = 'list_users'

        response = requests.get(self.BASE_URL+endpoint)
        users = response.text
        return users

    def get_event(self, id) -> dict:
        endpoint = "event/"

        response = requests.get(self.BASE_URL+endpoint+ id)
        event = dict(event.json())
        return event

    def get_events(self) -> list:
        endpoint = "list_event/"

        response = requests.get(self.BASE_URL+endpoint+self.user_id)
        if response.status_code == 200:
            events = list(response.json())
            return events
        return []


    def register(self, data):
        endpoint = "register"

        response = requests.post(self.BASE_URL+endpoint, json.dumps(data))

        return response.status_code

    def add_event(self, data):
        endpoint = "add_event/"

        response = requests.post(self.BASE_URL+endpoint, json.dumps(data))
        return response.status_code
    
    
    def edit_user(self, data):
        endpoint = "edit_user/"
        response = requests.put(self.BASE_URL+endpoint, json.dumps(data))
        return response.status_code

    def event(self, data):
        endpoint = "edit_event/"
        response = requests.put(self.BASE_URL+endpoint, json.dumps(data))
        return response.status_code


    def delete_user(self):
        endpoint = "del_user/"
        response = requests.put(self.BASE_URL+endpoint)
        return response.status_code

    def delete_event(self):
        endpoint = "del_event/"

        response = requests.delete(self.BASE_URL+endpoint)
        return response.status_code