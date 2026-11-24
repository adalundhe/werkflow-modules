from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .timestream_write_table import TimestreamWriteTable


class TimestreamWriteUpdateTableResponse(BaseModel):
    Table: TimestreamWriteTable | None = None
    ResponseMetadata: dict[str, Any] | None = None
