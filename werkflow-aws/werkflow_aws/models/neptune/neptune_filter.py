from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NeptuneFilter(BaseModel):
    Name: StrictStr
    Values: list[StrictStr]
