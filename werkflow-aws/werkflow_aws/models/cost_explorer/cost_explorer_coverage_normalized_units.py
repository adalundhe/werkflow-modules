from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CostExplorerCoverageNormalizedUnits(BaseModel):
    OnDemandNormalizedUnits: StrictStr | None = None
    ReservedNormalizedUnits: StrictStr | None = None
    TotalRunningNormalizedUnits: StrictStr | None = None
    CoverageNormalizedUnitsPercentage: StrictStr | None = None
