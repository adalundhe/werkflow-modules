from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ResilienceHubField(BaseModel):
    name: StrictStr
    aggregation: Literal['Min', 'Max', 'Sum', 'Avg', 'Count'] | None = None
