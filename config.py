from typing import Type, Optional, Literal
from os import getenv, environ

# Constants
APIChannel: Type = Literal["Develop", "Staging", "Production"]
SupportedDBS: Type = Literal["POSTGRESQL", "SQLITE"]

API_SERVICE_NAME: str = "auth-service"
API_VERSION: str = "0.0.1"
API_CHANNEL: APIChannel = "Develop"

# Optional
IS_DEBUG: Optional[bool] = None if getenv("FP_AUTH_IS_DEBUG") is None else bool("FP_AUTH_IS_DEBUG")

# Required
DB_ENGINE: SupportedDBS = "SQLITE"

POSTGRES_USER_NAME: str = environ["FP_AUTH_POSTGRES_USER_NAME"]
POSTGRES_PASSWORD: str = environ["FP_AUTH_POSTGRES_PASSWORD"]
POSTGRES_DB_NAME: str = environ["FP_AUTH_POSTGRES_DB_NAME"]
POSTGRES_HOST: str = environ["FP_AUTH_POSTGRES_HOST"]
POSTGRES_PORT: int = int(environ["FP_AUTH_POSTGRES_PORT"])

SQLITE_PATH: str = environ["FP_AUTH_SQLITE_PATH"]

FIREBASE_KEY_PATH: str = environ["FP_AUTH_FIREBASE_KEY_PATH"]

# Evaluated
ASYNC_POSTGRES_URL: str = f"postgresql+asyncpg://" \
                          f"{POSTGRES_USER_NAME}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB_NAME}"
SYNC_POSTGRES_URL: str = f"postgresql://" \
                         f"{POSTGRES_USER_NAME}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB_NAME}"

SYNC_SQLITE_URL: str = "sqlite:///" \
                       f"{SQLITE_PATH}"
