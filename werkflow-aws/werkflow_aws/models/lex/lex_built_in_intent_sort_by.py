from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class LexBuiltInIntentSortBy(BaseModel):
    attribute: Literal['IntentSignature']
    order: Literal['Ascending', 'Descending']
