from typing import Optional
from os import getenv, environ

# Optional
IS_DEBUG: Optional[bool] = None if getenv("FP_AUTH_IS_DEBUG") is None else bool("FP_AUTH_IS_DEBUG")

# Required
POSTGRES_USER_NAME: str = environ["FP_AUTH_POSTGRES_USER_NAME"]
POSTGRES_PASSWORD: str = environ["FP_AUTH_POSTGRES_PASSWORD"]
POSTGRES_DB_NAME: str = environ["FP_AUTH_POSTGRES_DB_NAME"]
POSTGRES_HOST: str = environ["FP_AUTH_POSTGRES_HOST"]
POSTGRES_PORT: int = int(environ["FP_AUTH_POSTGRES_PORT"])

# Evaluated
ASYNC_POSTGRES_URL: str = f"postgresql+asyncpg://" \
                    f"{POSTGRES_USER_NAME}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB_NAME}"
SYNC_POSTGRES_URL: str = f"postgresql://" \
                    f"{POSTGRES_USER_NAME}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB_NAME}"
