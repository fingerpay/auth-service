from firebase_admin import credentials
import firebase_admin

from config import FIREBASE_KEY_PATH


def initialize_firebase() -> None:
    cred = credentials.Certificate(FIREBASE_KEY_PATH)

    firebase_admin.initialize_app(cred)


def ensure_initialized() -> None:
    try:
        firebase_admin.get_app()

    except ValueError:
        initialize_firebase()
        ensure_initialized()

    return
