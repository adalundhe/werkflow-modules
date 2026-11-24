from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .timestream_write_database import TimestreamWriteDatabase


class TimestreamWriteListDatabasesResponse(BaseModel):
    Databases: list[TimestreamWriteDatabase] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
