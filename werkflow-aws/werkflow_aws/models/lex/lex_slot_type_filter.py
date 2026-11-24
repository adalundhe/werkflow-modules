from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class LexSlotTypeFilter(BaseModel):
    name: Literal['SlotTypeName', 'ExternalSourceType']
    values: list[StrictStr]
    operator: Literal['CO', 'EQ']
