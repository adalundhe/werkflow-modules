from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GluePartitionIndex(BaseModel):
    Keys: list[StrictStr]
    IndexName: StrictStr
