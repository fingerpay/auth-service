from typing import Literal, Tuple, get_args

from pydantic import BaseModel, Field, validator

VerificationStatus = Literal["valid", "invalid", "error", "unknown"]
ALLOWED_VERIFICATION_STATUS_VALUES: Tuple[str] = get_args(VerificationStatus)


class JWTVerification(BaseModel):
    is_authenticated: VerificationStatus = Field(
        title="Verification Status",
        description="A field indicates that the passed JWT token is valid or not",
        default="valid"
    )

    @validator('is_authenticated')
    def is_authenticated_must_be_literal(cls, v):
        if not (v in ALLOWED_VERIFICATION_STATUS_VALUES):
            raise ValueError(f"ValueError: expected {ALLOWED_VERIFICATION_STATUS_VALUES}, but got {v}")

        return v


class JWTVerificationResponse(JWTVerification):
    name: str = Field(
        title="User's Name",
        description="User's name provided from jwt token",
        example="Taro Yamada"
    )

    user_id: str = Field(
        title="Unique ID",
        description="Unique ID provided from JWT token, won't change even if the account's email is changed or so",
        example="xmzkvpKB8i2JLUeL6qn6TZmnCeRC"
    )

    is_registered: bool = Field(
        title="Is The User Registered to API Server",
        description="Indicates if the provided user is registered to this API Server or not",
        example=True,
        default=False
    )

    @validator("name")
    def name_must_have_value(cls, v):
        if (v == "") or (v is None):
            raise ValueError(f"ValueError: field 'name' must have a value")

        return v

    @validator("user_id")
    def user_id_must_have_value(cls, v):
        if (v == "") or (v is None):
            raise ValueError(f"ValueError: field 'user_id' must have a value")

        return v
