from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class LexBuiltInSlotTypeSortBy(BaseModel):
    attribute: Literal['SlotTypeSignature']
    order: Literal['Ascending', 'Descending']
