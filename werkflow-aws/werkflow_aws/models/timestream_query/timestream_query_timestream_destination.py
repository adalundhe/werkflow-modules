from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TimestreamQueryTimestreamDestination(BaseModel):
    DatabaseName: StrictStr | None = None
    TableName: StrictStr | None = None
