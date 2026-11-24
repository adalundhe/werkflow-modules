from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_monitoring_execution_summary import SageMakerMonitoringExecutionSummary
from .sage_maker_monitoring_schedule_config import SageMakerMonitoringScheduleConfig
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerMonitoringSchedule(BaseModel):
    MonitoringScheduleArn: StrictStr | None = None
    MonitoringScheduleName: StrictStr | None = None
    MonitoringScheduleStatus: StrictStr | None = None
    MonitoringType: StrictStr | None = None
    FailureReason: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    MonitoringScheduleConfig: SageMakerMonitoringScheduleConfig | None = None
    EndpointName: StrictStr | None = None
    LastMonitoringExecutionSummary: SageMakerMonitoringExecutionSummary | None = None
    Tags: list[SageMakerTagModel] | None = None
