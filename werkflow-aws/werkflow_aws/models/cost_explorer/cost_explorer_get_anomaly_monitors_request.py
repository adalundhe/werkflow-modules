from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CostExplorerGetAnomalyMonitorsRequest(BaseModel):
    MonitorArnList: list[StrictStr] | None = None
    NextPageToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
