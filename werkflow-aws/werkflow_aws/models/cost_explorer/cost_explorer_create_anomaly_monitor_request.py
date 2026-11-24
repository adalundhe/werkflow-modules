from __future__ import annotations
from pydantic import BaseModel
from .cost_explorer_anomaly_monitor import CostExplorerAnomalyMonitor
from .cost_explorer_resource_tag import CostExplorerResourceTag


class CostExplorerCreateAnomalyMonitorRequest(BaseModel):
    AnomalyMonitor: CostExplorerAnomalyMonitor
    ResourceTags: list[CostExplorerResourceTag] | None = None
