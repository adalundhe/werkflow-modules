from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class LexExportSortBy(BaseModel):
    attribute: Literal['LastUpdatedDateTime']
    order: Literal['Ascending', 'Descending']
