import uuid

from sqlalchemy import types
from sqlalchemy.dialects.mysql.base import MSBinary
from sqlalchemy.schema import Column

DEFAULT_UUID_COLUMN_NAME: str = "id"


class UUID(types.TypeDecorator):
    impl = MSBinary

    def __init__(self):
        self.impl.length = 16
        types.TypeDecorator.__init__(self, length=self.impl.length)

    def process_bind_param(self, value, dialect=None):
        if value and isinstance(value, uuid.UUID):
            return value.bytes
        elif value and not isinstance(value, uuid.UUID):
            raise ValueError(f"value {value} is not a valid uuid.UUID")
        else:
            return None

    def process_result_value(self, value, dialect=None):
        if value:
            return uuid.UUID(bytes=value)
        else:
            return None

    def is_mutable(self):
        return False


def UUIDColumn(column_name: str = DEFAULT_UUID_COLUMN_NAME, **kwargs):
    return Column(column_name, UUID(), primary_key=True, default=uuid.uuid4, **kwargs)
