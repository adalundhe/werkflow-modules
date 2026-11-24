from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerStopMonitoringScheduleRequest(BaseModel):
    MonitoringScheduleName: StrictStr
