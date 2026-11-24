from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TimestreamWriteDeleteTableRequest(BaseModel):
    DatabaseName: StrictStr
    TableName: StrictStr
