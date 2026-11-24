from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSFilterModel(BaseModel):
    Name: StrictStr
    Values: list[StrictStr]
