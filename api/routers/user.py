from typing import Optional, Dict

from fastapi import APIRouter, Depends, HTTPException
from pydantic import EmailStr
from sqlalchemy.orm import Session

from api.db import SessionLocal
from api.auth.user import get_user
from api.cruds.user import create_user, get_user_by_user_id
from api.models.user import User as UserModel
from api.schemas.user import User as UserSchema
from api.schemas.user import UserCreateRequest
from api.schemas.user import RegisteredUserResponse

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/user/register", response_model=RegisteredUserResponse)
def register_user(
        user: Dict = Depends(get_user),
        db: Session = Depends(get_db)):
    name: str = user["name"]
    email: str = user["email"]
    user_id: str = user["user_id"]
    picture: str = user["picture"]

    if get_user_by_user_id(db, user_id) is not None:
        raise HTTPException(
            status_code=400,
            detail="The user with this uid is already registered"
        )

    request: UserCreateRequest = UserCreateRequest(
        name=name, email=EmailStr(email), user_id=user_id, picture=picture
    )

    created: UserModel = create_user(db, request)

    response: RegisteredUserResponse = RegisteredUserResponse(
        id=str(created.id), name=created.name, email=EmailStr(created.email), user_id=created.user_id,
        picture=created.picture
    )

    return response


@router.get("/user/me", response_model=RegisteredUserResponse)
def my_infos(
        user: Dict = Depends(get_user),
        db: Session = Depends(get_db)):
    name: str = user["name"]
    email: str = user["email"]
    user_id: str = user["user_id"]
    picture: str = user["picture"]

    result: Optional[UserModel] = get_user_by_user_id(db, user_id)

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="This user is not registered"
        )

    response: RegisteredUserResponse = RegisteredUserResponse(
        id=str(result.id), name=result.name, email=EmailStr(result.email), user_id=result.user_id,
        picture=result.picture
    )

    return response
