from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSFilter(BaseModel):
    Name: StrictStr
    Values: list[StrictStr]
