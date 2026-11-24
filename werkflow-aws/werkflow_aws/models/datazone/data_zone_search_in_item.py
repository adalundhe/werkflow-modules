from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneSearchInItem(BaseModel):
    attribute: StrictStr
