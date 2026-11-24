from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeleteMonitoringScheduleRequest(BaseModel):
    MonitoringScheduleName: StrictStr
