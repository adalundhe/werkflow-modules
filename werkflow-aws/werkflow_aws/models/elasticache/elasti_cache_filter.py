from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ElastiCacheFilter(BaseModel):
    Name: StrictStr
    Values: list[StrictStr]
