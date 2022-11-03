import random
import uvicorn

from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware import Middleware

from config import settings

MIDDLEWARE = [
    Middleware(CORSMiddleware,
               allow_origins=[
                   str(origin) for origin in settings.BACKEND_CORS_ORIGINS
               ],
               allow_credentials=True,
               allow_methods=['GET, POST'],
               allow_headers=["*"])
]

router = APIRouter()

api = FastAPI(
    title=settings.PROJECT_NAME,
    contact={
        "name": "Ian Meinert",
    },
    docs_url="/documentation",
    redoc_url=None,
    middleware=MIDDLEWARE,
    openapi_url="/openapi.json",
)


@router.get('/home', name='home', status_code=200)
async def index():
    return {"text": "My home page"}


@router.get('/about', name='about', status_code=200)
async def index():
    return {"text": "My about page"}


@router.get('/resume', name='resume', status_code=200)
async def index():
    return {"text": "My resume page"}


@router.get("/rand", name='rand', status_code=200)
async def rand():
    return random.randint(0, 100)

api.include_router(router)

if __name__ == '__main__':
    uvicorn.run(app='server:api', host=settings.HOST,
                port=settings.PORT, reload=True)
