from sqlalchemy import Column, String

from sqlalchemy_utils import EmailType
from sqlalchemy_utils import URLType

from api.cruds.types.uuid import UUIDColumn
from api.models.mixin.timestamp import TimeStampMixin

from api.db import Base


class User(Base, TimeStampMixin):
    __tablename__: str = "users"

    id = UUIDColumn(
        column_name="id"
    )

    name = Column(
        String,
        nullable=False
    )

    email = Column(
        EmailType,
        nullable=False, unique=True
    )

    user_id = Column(
        String,
        nullable=False, unique=True
    )

    picture = Column(
        URLType,
        nullable=False
    )
