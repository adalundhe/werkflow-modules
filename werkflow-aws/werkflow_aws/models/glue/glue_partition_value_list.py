from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GluePartitionValueList(BaseModel):
    Values: list[StrictStr] | None = None
