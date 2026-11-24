from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .timestream_query_type import TimestreamQueryType


class TimestreamQuerySelectColumn(BaseModel):
    Name: StrictStr | None = None
    Type: TimestreamQueryType | None = None
    DatabaseName: StrictStr | None = None
    TableName: StrictStr | None = None
    Aliased: StrictBool | None = None
