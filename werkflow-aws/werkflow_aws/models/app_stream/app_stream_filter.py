from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamFilter(BaseModel):
    Name: StrictStr
    Values: list[StrictStr]
