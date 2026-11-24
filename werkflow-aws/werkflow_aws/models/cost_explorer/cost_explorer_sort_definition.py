from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CostExplorerSortDefinition(BaseModel):
    Key: StrictStr
    SortOrder: Literal['ASCENDING', 'DESCENDING'] | None = None
