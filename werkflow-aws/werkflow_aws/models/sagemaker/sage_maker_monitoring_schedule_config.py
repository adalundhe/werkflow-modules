from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_monitoring_job_definition import SageMakerMonitoringJobDefinition
from .sage_maker_schedule_config import SageMakerScheduleConfig


class SageMakerMonitoringScheduleConfig(BaseModel):
    ScheduleConfig: SageMakerScheduleConfig | None = None
    MonitoringJobDefinition: SageMakerMonitoringJobDefinition | None = None
    MonitoringJobDefinitionName: StrictStr | None = None
    MonitoringType: StrictStr | None = None
