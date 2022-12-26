from typing import Optional, Dict

from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends

from api.db import SessionLocal
from api.auth.user import get_user
from api.schemas.jwt import JWTVerificationResponse
from api.models.user import User as UserModel
from api.cruds.user import get_user_by_user_id

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/jwt/verify", response_model=JWTVerificationResponse)
async def verify_jwt(user: Dict = Depends(get_user), db: Session = Depends(get_db)):
    name: str = user["name"]
    user_id: str = user["user_id"]

    result: Optional[UserModel] = get_user_by_user_id(db, user_id)

    is_registered: bool = bool(result)

    response: JWTVerificationResponse = JWTVerificationResponse(
        is_authenticated="valid", name=name, user_id=user_id, is_registered=is_registered
    )

    return response
