from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerListMonitoringAlertsRequest(BaseModel):
    MonitoringScheduleName: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
