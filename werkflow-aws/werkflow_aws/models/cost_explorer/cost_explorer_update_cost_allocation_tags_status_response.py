from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cost_explorer_update_cost_allocation_tags_status_error import CostExplorerUpdateCostAllocationTagsStatusError


class CostExplorerUpdateCostAllocationTagsStatusResponse(BaseModel):
    Errors: list[CostExplorerUpdateCostAllocationTagsStatusError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
