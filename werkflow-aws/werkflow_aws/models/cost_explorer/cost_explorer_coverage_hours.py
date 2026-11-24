from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CostExplorerCoverageHours(BaseModel):
    OnDemandHours: StrictStr | None = None
    ReservedHours: StrictStr | None = None
    TotalRunningHours: StrictStr | None = None
    CoverageHoursPercentage: StrictStr | None = None
