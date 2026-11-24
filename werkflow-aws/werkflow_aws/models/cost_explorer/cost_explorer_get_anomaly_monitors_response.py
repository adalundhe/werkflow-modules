from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cost_explorer_anomaly_monitor import CostExplorerAnomalyMonitor


class CostExplorerGetAnomalyMonitorsResponse(BaseModel):
    AnomalyMonitors: list[CostExplorerAnomalyMonitor] | None = None
    NextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
