from typing import Dict

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException, status, Response
from firebase_admin import auth

from api.firebase import ensure_initialized


def get_jwt_payload(res: Response, credential: HTTPAuthorizationCredentials = Depends(HTTPBearer(auto_error=True))):
    ensure_initialized()

    if (credential is None) or (credential == ""):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Bearer authentication required",
            headers={'WWW-Authenticate': 'Bearer realm="auth_required"'},
        )

    try:
        auth.verify_id_token(credential.credentials)

    except Exception as err:
        print(f"Failed to decode jwt!\n"
              f"The following exception has risen:\n"
              f"{err}")

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid authentication credentials",
            headers={'WWW-Authenticate': 'Bearer error="invalid_token"'},
        )

    res.headers['WWW-Authenticate'] = 'Bearer realm="auth_required"'

    return credential.credentials


def get_user(res: Response, credential: HTTPAuthorizationCredentials = Depends(HTTPBearer(auto_error=True))):
    ensure_initialized()

    if (credential is None) or (credential == ""):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Bearer authentication required",
            headers={'WWW-Authenticate': 'Bearer realm="auth_required"'},
        )

    try:
        decoded_token: Dict = auth.verify_id_token(credential.credentials)

    except Exception as err:
        print(f"Failed to decode jwt!\n"
              f"The following exception has risen:\n"
              f"{err}")

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid authentication credentials",
            headers={'WWW-Authenticate': 'Bearer error="invalid_token"'},
        )

    res.headers['WWW-Authenticate'] = 'Bearer realm="auth_required"'

    return decoded_token
