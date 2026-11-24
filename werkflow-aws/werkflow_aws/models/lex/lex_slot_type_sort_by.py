from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class LexSlotTypeSortBy(BaseModel):
    attribute: Literal['SlotTypeName', 'LastUpdatedDateTime']
    order: Literal['Ascending', 'Descending']
