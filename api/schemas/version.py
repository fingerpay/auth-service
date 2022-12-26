from typing import Tuple, get_args

from pydantic import BaseModel, Field, validator

import config
from config import APIChannel
from config import API_SERVICE_NAME
from config import API_VERSION
from config import API_CHANNEL

ALLOWED_APICHANNEL_VALUES: Tuple[str] = get_args(APIChannel)


class ServerVersionResponse(BaseModel):
    api_service_name: str = Field(
        title="My Service Name",
        description="Describes which service to serve",
        default=config.API_SERVICE_NAME,
        sample=config.API_SERVICE_NAME
    )

    api_version: str = Field(
        title="API Version",
        description="My version of API, following semantic versioning rule",
        default=config.API_VERSION,
        sample=config.API_VERSION
    )

    api_channel: APIChannel = Field(
        title="API Channel",
        description=f"Describes which channel to belonging to, the channels are {ALLOWED_APICHANNEL_VALUES}",
        default=config.API_CHANNEL,
        sample=config.API_CHANNEL
    )
