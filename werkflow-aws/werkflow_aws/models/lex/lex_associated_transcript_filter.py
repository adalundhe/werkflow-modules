from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class LexAssociatedTranscriptFilter(BaseModel):
    name: Literal['IntentId', 'SlotTypeId']
    values: list[StrictStr]
