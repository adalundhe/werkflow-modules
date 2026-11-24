from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cost_explorer_cost_allocation_tag_backfill_request import CostExplorerCostAllocationTagBackfillRequest


class CostExplorerStartCostAllocationTagBackfillResponse(BaseModel):
    BackfillRequest: CostExplorerCostAllocationTagBackfillRequest | None = None
    ResponseMetadata: dict[str, Any] | None = None
