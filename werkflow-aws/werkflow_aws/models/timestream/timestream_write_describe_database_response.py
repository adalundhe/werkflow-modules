from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .timestream_write_database import TimestreamWriteDatabase


class TimestreamWriteDescribeDatabaseResponse(BaseModel):
    Database: TimestreamWriteDatabase | None = None
    ResponseMetadata: dict[str, Any] | None = None
