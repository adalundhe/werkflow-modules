from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class DataZoneFilter(BaseModel):
    attribute: StrictStr
    value: StrictStr | None = None
    intValue: StrictInt | None = None
    operator: Literal['EQ', 'LE', 'LT', 'GE', 'GT', 'TEXT_SEARCH'] | None = None
