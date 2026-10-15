import httpx
from contextlib import asynccontextmanager
from fastapi import FastAPI

N=10

@asynccontextmanager
async def lifespan(app: FastAPI):
    print('app starting')
    app.state.http = httpx.AsyncClient(timeout=10,limits=httpx.Limits(max_connections=N, max_keepalive_connections=N))

    yield

    await app.state.http.aclose()  
    print('shutting down....')