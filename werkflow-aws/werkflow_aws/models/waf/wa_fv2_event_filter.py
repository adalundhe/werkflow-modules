from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class WAFv2EventFilter(BaseModel):
    Name: Literal['EVENT_CATEGORY', 'RESOURCE_ARN']
    Values: list[StrictStr]
