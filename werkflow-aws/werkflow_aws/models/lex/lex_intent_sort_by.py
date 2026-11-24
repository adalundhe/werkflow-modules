from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class LexIntentSortBy(BaseModel):
    attribute: Literal['IntentName', 'LastUpdatedDateTime']
    order: Literal['Ascending', 'Descending']
