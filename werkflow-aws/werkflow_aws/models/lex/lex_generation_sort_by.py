from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class LexGenerationSortBy(BaseModel):
    attribute: Literal['creationStartTime', 'lastUpdatedTime']
    order: Literal['Ascending', 'Descending']
