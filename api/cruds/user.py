from typing import Optional, Tuple

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.orm import Session

import api.models.user as user_model
import api.schemas.user as user_schema


def create_user(db: Session, create_request: user_schema.UserCreateRequest) -> user_model.User:
    user: user_model.User = user_model.User(
        name=create_request.name,
        email=create_request.email,
        user_id=create_request.user_id,
        picture=create_request.picture
    )

    db.add(user)

    db.commit()
    db.refresh(user)

    return user


def get_user_by_user_id(db: Session, user_id: str) -> Optional[user_model.User]:
    result: Result = db.execute(
        select(user_model.User).filter(user_model.User.user_id == user_id)
    )

    users: Optional[Tuple[user_model.User]] = result.first()

    first: Optional[user_model.User] = None

    # 要素が一つであってもtupleで返却されるので１つ目の要素を取り出す
    if users is not None:
        first: Optional[user_model.User] = users[0]

    return first
