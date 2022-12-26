from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import func


class TimeStampMixin(object):
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), nullable=False)
