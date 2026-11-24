from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WAFv2MonetizationFilter(BaseModel):
    Name: StrictStr
    Values: list[StrictStr]
