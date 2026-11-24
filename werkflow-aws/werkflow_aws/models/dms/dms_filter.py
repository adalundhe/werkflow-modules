from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSFilter(BaseModel):
    Name: StrictStr
    Values: list[StrictStr]
