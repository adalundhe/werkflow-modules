from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CostExplorerSavingsPlansSavings(BaseModel):
    NetSavings: StrictStr | None = None
    OnDemandCostEquivalent: StrictStr | None = None
