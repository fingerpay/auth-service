from pydantic import BaseModel, Field

from api.cruds.types.uuid import UUIDColumn


class Fingerprint(BaseModel):
    id = UUIDColumn(
        column_name="id"
    )


class FingerprintRegisterRequest(Fingerprint):
    # the field 'id' is not included in request schema
    id: None = None
    
    token: str = Field(
        title="Token",
        description="Tentative token to register each fingerprints and a user",
        nullable=True
    )

    registration_device: str = Field(
        title="Device",
        description="The device name which registers a fingerprint at the first time",
        nullable=False
    )

    place: int = Field(
        title="Place ID",
        description="Place ID which is a id of a model is stored",
        nullable=False
    )

    characteristics: bytes = Field(
        title="Characteristics",
        description="Characteristics of the fingerprint, should be hashed or encrypted",
        nullable=True
    )

    hash: str = Field(
        title="Hash of Fingerprint",
        description="Hash value evaluated from characteristics data, should be secret",
        nullable=False
    )
