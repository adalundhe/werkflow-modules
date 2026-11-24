from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerStartMonitoringScheduleRequest(BaseModel):
    MonitoringScheduleName: StrictStr
