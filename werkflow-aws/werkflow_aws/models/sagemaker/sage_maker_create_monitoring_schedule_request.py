from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_monitoring_schedule_config import SageMakerMonitoringScheduleConfig
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateMonitoringScheduleRequest(BaseModel):
    MonitoringScheduleName: StrictStr
    MonitoringScheduleConfig: SageMakerMonitoringScheduleConfig
    Tags: list[SageMakerTagModel] | None = None
