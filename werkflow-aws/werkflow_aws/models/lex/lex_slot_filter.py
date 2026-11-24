from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class LexSlotFilter(BaseModel):
    name: Literal['SlotName']
    values: list[StrictStr]
    operator: Literal['CO', 'EQ']
