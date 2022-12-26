from sqlalchemy import create_engine

from config import SYNC_SQLITE_URL

from api.models.user import Base

DB_URL = SYNC_SQLITE_URL
engine = create_engine(DB_URL, echo=True)


def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()
