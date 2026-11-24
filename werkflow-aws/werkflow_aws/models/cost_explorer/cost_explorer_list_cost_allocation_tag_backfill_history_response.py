from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cost_explorer_cost_allocation_tag_backfill_request import CostExplorerCostAllocationTagBackfillRequest


class CostExplorerListCostAllocationTagBackfillHistoryResponse(BaseModel):
    BackfillRequests: list[CostExplorerCostAllocationTagBackfillRequest] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
