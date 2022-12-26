from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    name: str = Field(
        title="Name",
        description="Name of the user, provided from JWT",
        nullable=False
    )

    email: EmailStr = Field(
        title="Email",
        description="Email of the user, provided from JWT",
        nullable=False
    )

    user_id: str = Field(
        title="Unique ID",
        description="Unique ID of the user, provided from JWT",
        nullable=False
    )

    picture: str = Field(
        title="Profile Picture",
        description="Picture URL of the user, provided from JWT",
        nullable=False
    )


class UserCreateRequest(User):
    pass


class RegisteredUserResponse(User):
    id: str = Field(
        title="UUID",
        description="UUID for the user, never changes",
        nullable=False
    )
