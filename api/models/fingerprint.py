from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import validates

from api.cruds.types.bytes import HexByteString

from api.cruds.types.uuid import UUIDColumn
from api.models.mixin.timestamp import TimeStampMixin

from api.db import Base


class FingerPrint(Base, TimeStampMixin):
    __tablename__: str = "fingerprints"

    TOKEN_BYTES_LENGTH: int = 64
    TOKEN_STR_LENGTH: int = 86

    id = UUIDColumn(
        column_name="id"
    )

    token = Column(
        String,
        nullable=False, unique=True
    )

    device = Column(
        String,
        nullable=False, unique=False
    )

    place = Column(
        Integer,
        nullable=False, unique=False
    )

    characteristics = Column(
        HexByteString,
        nullable=True, unique=True
    )

    hash = Column(
        String,
        nullable=False, unique=True
    )

    @validates("token")
    def validate_token(self, key, value):
        if len(value) == FingerPrint.TOKEN_STR_LENGTH:
            raise ValueError(f"length of token must be {FingerPrint.TOKEN_STR_LENGTH},"
                             f"but got {len(value)}")

        return value
