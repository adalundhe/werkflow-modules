from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cost_explorer_cost_allocation_tag import CostExplorerCostAllocationTag


class CostExplorerListCostAllocationTagsResponse(BaseModel):
    CostAllocationTags: list[CostExplorerCostAllocationTag] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
