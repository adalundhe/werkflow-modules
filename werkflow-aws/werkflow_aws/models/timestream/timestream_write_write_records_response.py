from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .timestream_write_records_ingested import TimestreamWriteRecordsIngested


class TimestreamWriteWriteRecordsResponse(BaseModel):
    RecordsIngested: TimestreamWriteRecordsIngested | None = None
    ResponseMetadata: dict[str, Any] | None = None
