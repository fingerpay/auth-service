from typing import Optional, TypeVar
from os import getenv

T = TypeVar('T')

# Optional
IS_DEBUG: Optional[bool] = None if getenv("FP_AUTH_IS_DEBUG") is None else bool("FP_AUTH_IS_DEBUG")

# Required
POSTGRES_USER_NAME: str = getenv("FP_AUTH_POSTGRES_USER_NAME")
POSTGRES_PASSWORD: str = getenv("FP_AUTH_POSTGRES_PASSWORD")
POSTGRES_DB_NAME: str = getenv("FP_AUTH_POSTGRES_DB_NAME")
