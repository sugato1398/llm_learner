from fastapi import APIRouter, Depends
from config import Settings, get_settings
from pydantic import BaseModel

class Contact(BaseModel):
    user: str

contactRouter = APIRouter()

names = ['name1','name2','name3']


@contactRouter.get('/{user_id}/contacts')
def getContacts(user_id: str,limit:int = 20,settings: Settings = Depends(get_settings) ):
    print( settings.database_url)
    maxlen = min(len(names),limit)
    return names[:maxlen]



@contactRouter.post('/{user_id}/contacts')
def addContact(user_id:str , contact: Contact):
    names.append(contact.user)
    return "added"

