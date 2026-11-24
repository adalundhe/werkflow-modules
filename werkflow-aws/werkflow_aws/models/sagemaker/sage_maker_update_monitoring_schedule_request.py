from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_monitoring_schedule_config import SageMakerMonitoringScheduleConfig


class SageMakerUpdateMonitoringScheduleRequest(BaseModel):
    MonitoringScheduleName: StrictStr
    MonitoringScheduleConfig: SageMakerMonitoringScheduleConfig
