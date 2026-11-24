from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cost_explorer_coverage import CostExplorerCoverage


class CostExplorerReservationCoverageGroup(BaseModel):
    Attributes: dict[StrictStr, StrictStr] | None = None
    Coverage: CostExplorerCoverage | None = None
