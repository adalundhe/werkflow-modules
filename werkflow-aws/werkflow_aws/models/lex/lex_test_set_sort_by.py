from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class LexTestSetSortBy(BaseModel):
    attribute: Literal['TestSetName', 'LastUpdatedDateTime']
    order: Literal['Ascending', 'Descending']
