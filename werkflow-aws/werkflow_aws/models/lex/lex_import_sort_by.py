from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class LexImportSortBy(BaseModel):
    attribute: Literal['LastUpdatedDateTime']
    order: Literal['Ascending', 'Descending']
