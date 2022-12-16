from fastapi import FastAPI, Depends
from api.user import get_user

app = FastAPI()


@app.get("/me")
async def hello_user(user=Depends(get_user)):
    return {"isAuthenticated": True, "name": user["name"], "user_id": user["user_id"], "uid": user["uid"]}
