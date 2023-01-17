from pydantic import BaseModel


class User(BaseModel):
    userid: int
    name: str
    email: str
    password: str
    status: int

class Users(BaseModel):
    users:list[User]
    count:int