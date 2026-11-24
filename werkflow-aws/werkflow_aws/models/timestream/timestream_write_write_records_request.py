from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .timestream_write_record import TimestreamWriteRecord


class TimestreamWriteWriteRecordsRequest(BaseModel):
    DatabaseName: StrictStr
    TableName: StrictStr
    Records: list[TimestreamWriteRecord]
    CommonAttributes: TimestreamWriteRecord | None = None
