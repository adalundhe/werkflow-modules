from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class LexAggregatedUtterancesSortBy(BaseModel):
    attribute: Literal['HitCount', 'MissedCount']
    order: Literal['Ascending', 'Descending']
