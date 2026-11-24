from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .timestream_write_table import TimestreamWriteTable


class TimestreamWriteListTablesResponse(BaseModel):
    Tables: list[TimestreamWriteTable] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
