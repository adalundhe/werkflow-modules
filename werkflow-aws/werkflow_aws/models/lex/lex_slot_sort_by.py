from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class LexSlotSortBy(BaseModel):
    attribute: Literal['SlotName', 'LastUpdatedDateTime']
    order: Literal['Ascending', 'Descending']
