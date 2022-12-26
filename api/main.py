from fastapi import FastAPI

from api.routers import jwt
from api.routers import about
from api.routers import user

app = FastAPI()
app.include_router(jwt.router)
app.include_router(about.router)
app.include_router(user.router)
