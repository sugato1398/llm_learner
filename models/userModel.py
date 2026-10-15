from pydantic import BaseModel, Field, ValidationError

class User(BaseModel):
    id: int
    name:str = "anonymous"
    email:str
    age:int = Field( gt=0,le=150)



class StreetAddress(BaseModel):
    line1: str
    city: str
    postcode: str

class Person(BaseModel):
    name: str
    home: StreetAddress
    phone: list[str]

class Team(BaseModel):
    name:str
    members: list[Person]
    leads: dict[str,Person]