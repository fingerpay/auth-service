from typing import Type, Tuple, Literal, get_args

from pydantic import BaseModel, Field

import config

ServerHealthStatus: Type = Literal["OK", "DOWN"]

ALLOWED_SERVER_HEALTH_STATUS_VALUES: Tuple[str] = get_args(ServerHealthStatus)


class ServerHealthStatusResponse(BaseModel):
    health: ServerHealthStatus = Field(
        title="Health of The Server",
        description=f"Current health status of this server, it can be {ALLOWED_SERVER_HEALTH_STATUS_VALUES}",
        default="OK",
        sample="OK"
    )
