from fastapi import APIRouter, Depends, Request
from config import Settings, get_settings
from pydantic import BaseModel
import time
import asyncio

DELAY=1

class Contact(BaseModel):
    user: str

class Message(BaseModel):
    msg: str

contactRouter = APIRouter()

names = ['name1','name2','name3']


@contactRouter.get('/{user_id}/contacts')
def getContacts(user_id: str,limit:int = 20,settings: Settings = Depends(get_settings) ):
    print( settings.database_url)
    time.sleep(DELAY)
    maxlen = min(len(names),limit)
    return names[:maxlen]



@contactRouter.post('/{user_id}/contacts')
def addContact(user_id:str , contact: Contact):
    time.sleep(DELAY)
    names.append(contact.user)
    return "added"



@contactRouter.get('/{user_id}/contacts/v2')
async def getContactsv2(user_id: str,limit:int = 20,settings: Settings = Depends(get_settings) ):
    print( settings.database_url)
    await asyncio.sleep(DELAY)
    maxlen = min(len(names),limit)
    return names[:maxlen]



@contactRouter.post('/{user_id}/contacts/v2')
async def addContactv2(user_id:str , contact: Contact):
    await asyncio.sleep(DELAY)
    names.append(contact.user)
    return "added"


@contactRouter.post('/chat')
async def claudechat(message: Message, request: Request, settings: Settings = Depends(get_settings)) -> dict :
    # do the claude anthropic call
    headers = { 'x-api-key': settings.anthropic_api_key, 'anthropic-version': '2023-06-01'}
    body = {
        'max_tokens': 1024,
        'model': 'claude-sonnet-5-5',
        'messages': [{
            'content': message.msg,
            'role': 'user'
        }]
    }
    client = request.app.state.http
    result = await client.post('https://api.anthropic.com/v1/messages', headers=headers,json=body)

    result.raise_for_status()
    data = result.json()

    return data


@contactRouter.post('/chatToken')
async def chattoken(message: Message, request: Request, settings: Settings = Depends(get_settings)) -> dict :
    headers = { 'x-api-key': settings.anthropic_api_key, 'anthropic-version': '2023-06-01'}
    body = {
        
        'model': 'claude-sonnet-5-5',
        'messages': [{
            'content': message.msg,
            'role': 'user'
        }]
    }
    client = request.app.state.http
    result = await client.post('https://api.anthropic.com/v1/messages/count_tokens', headers=headers,json=body)

    result.raise_for_status()
    data = result.json()

    return data