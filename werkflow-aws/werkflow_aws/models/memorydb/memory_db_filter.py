from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MemoryDBFilter(BaseModel):
    Name: StrictStr
    Values: list[StrictStr]
