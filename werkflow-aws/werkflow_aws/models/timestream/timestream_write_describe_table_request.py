from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TimestreamWriteDescribeTableRequest(BaseModel):
    DatabaseName: StrictStr
    TableName: StrictStr
