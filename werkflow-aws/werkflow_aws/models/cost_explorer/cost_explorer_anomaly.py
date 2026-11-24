from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cost_explorer_anomaly_score import CostExplorerAnomalyScore
from .cost_explorer_impact import CostExplorerImpact
from .cost_explorer_root_cause import CostExplorerRootCause


class CostExplorerAnomaly(BaseModel):
    AnomalyId: StrictStr | None = None
    AnomalyStartDate: StrictStr | None = None
    AnomalyEndDate: StrictStr | None = None
    DimensionValue: StrictStr | None = None
    RootCauses: list[CostExplorerRootCause] | None = None
    AnomalyScore: CostExplorerAnomalyScore | None = None
    Impact: CostExplorerImpact | None = None
    MonitorArn: StrictStr | None = None
    Feedback: StrictStr | None = None
