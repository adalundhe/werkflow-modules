from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .timestream_query_type import TimestreamQueryType


class TimestreamQueryColumnInfo(BaseModel):
    Name: StrictStr | None = None
    Type: TimestreamQueryType | None = None
