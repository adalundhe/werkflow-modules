from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CostExplorerCostAllocationTagStatusEntry(BaseModel):
    TagKey: StrictStr
    Status: Literal['Active', 'Inactive']
