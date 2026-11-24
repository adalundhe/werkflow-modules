from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class LexTestExecutionSortBy(BaseModel):
    attribute: Literal['TestSetName', 'CreationDateTime']
    order: Literal['Ascending', 'Descending']
