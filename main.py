from fastapi import FastAPI
from controller.GetContact import contactRouter
import uvicorn

app = FastAPI()

app.include_router(contactRouter)

@app.get('/health')
def getHealth():
    return {'status': 'ok'}


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)