from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TimestreamWriteDescribeDatabaseRequest(BaseModel):
    DatabaseName: StrictStr
