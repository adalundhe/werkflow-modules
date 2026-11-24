from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictFloat, StrictInt


class DataZoneRejectRule(BaseModel):
    rule: Literal['ALL', 'NONE'] | None = None
    threshold: StrictFloat | StrictInt | None = None
