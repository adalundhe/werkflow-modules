from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeMonitoringScheduleRequest(BaseModel):
    MonitoringScheduleName: StrictStr
