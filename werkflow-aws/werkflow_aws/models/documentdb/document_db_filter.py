from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DocumentDBFilter(BaseModel):
    Name: StrictStr
    Values: list[StrictStr]
