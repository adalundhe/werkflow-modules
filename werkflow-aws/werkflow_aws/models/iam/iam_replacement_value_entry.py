from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMReplacementValueEntry(BaseModel):
    Values: list[StrictStr]
