from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CostExplorerSavingsPlansCoverageData(BaseModel):
    SpendCoveredBySavingsPlans: StrictStr | None = None
    OnDemandCost: StrictStr | None = None
    TotalCost: StrictStr | None = None
    CoveragePercentage: StrictStr | None = None
