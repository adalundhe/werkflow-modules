from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CostExplorerUpdateAnomalyMonitorRequest(BaseModel):
    MonitorArn: StrictStr
    MonitorName: StrictStr | None = None
