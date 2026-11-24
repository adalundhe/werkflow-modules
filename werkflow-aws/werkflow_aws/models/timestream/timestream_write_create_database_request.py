from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .timestream_write_tag import TimestreamWriteTag


class TimestreamWriteCreateDatabaseRequest(BaseModel):
    DatabaseName: StrictStr
    KmsKeyId: StrictStr | None = None
    Tags: list[TimestreamWriteTag] | None = None
