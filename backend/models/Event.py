from pydantic import BaseModel


class Event(BaseModel):
    eventid: int
    title: str
    description: str
    date: str
    user: int

class Events(BaseModel):
    events: list[Event]
    count: int