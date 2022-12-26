from fastapi import APIRouter

from api.schemas.version import ServerVersionResponse
from api.schemas.health import ServerHealthStatusResponse

router = APIRouter()


@router.get("/about/version", response_model=ServerVersionResponse)
async def server_version():
    response: ServerVersionResponse = ServerVersionResponse()

    return response


@router.get("/about/health", response_model=ServerHealthStatusResponse)
async def server_health():
    response: ServerHealthStatusResponse = ServerHealthStatusResponse()

    return response
