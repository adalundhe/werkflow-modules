from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cost_explorer_root_cause_impact import CostExplorerRootCauseImpact


class CostExplorerRootCause(BaseModel):
    Service: StrictStr | None = None
    Region: StrictStr | None = None
    LinkedAccount: StrictStr | None = None
    LinkedAccountName: StrictStr | None = None
    UsageType: StrictStr | None = None
    Impact: CostExplorerRootCauseImpact | None = None
