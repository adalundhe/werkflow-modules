from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cost_explorer_coverage import CostExplorerCoverage
from .cost_explorer_coverage_by_time import CostExplorerCoverageByTime


class CostExplorerGetReservationCoverageResponse(BaseModel):
    CoveragesByTime: list[CostExplorerCoverageByTime] | None = None
    Total: CostExplorerCoverage | None = None
    NextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
