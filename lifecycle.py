import httpx
from contextlib import asynccontextmanager
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    print('app starting')
    app.state.http = httpx.AsyncClient(timeout=10)

    yield

    await app.state.http.aclose()  
    print('shutting down....')