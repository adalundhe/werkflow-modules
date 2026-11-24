from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class GlueSearchSort(BaseModel):
    Attribute: StrictStr
    Order: Literal['ASCENDING', 'DESCENDING'] | None = None
