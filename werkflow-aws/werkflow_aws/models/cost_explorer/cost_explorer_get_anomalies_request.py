from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .cost_explorer_anomaly_date_interval import CostExplorerAnomalyDateInterval
from .cost_explorer_total_impact_filter import CostExplorerTotalImpactFilter


class CostExplorerGetAnomaliesRequest(BaseModel):
    DateInterval: CostExplorerAnomalyDateInterval
    MonitorArn: StrictStr | None = None
    Feedback: Literal['YES', 'NO', 'PLANNED_ACTIVITY'] | None = None
    TotalImpact: CostExplorerTotalImpactFilter | None = None
    NextPageToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
