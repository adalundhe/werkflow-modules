from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class DataZoneSearchSort(BaseModel):
    attribute: StrictStr
    order: Literal['ASCENDING', 'DESCENDING'] | None = None
