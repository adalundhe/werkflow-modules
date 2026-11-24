from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CostExplorerSavingsPlansUtilization(BaseModel):
    TotalCommitment: StrictStr | None = None
    UsedCommitment: StrictStr | None = None
    UnusedCommitment: StrictStr | None = None
    UtilizationPercentage: StrictStr | None = None
