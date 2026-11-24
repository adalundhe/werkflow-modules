from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_monitoring_execution_summary import SageMakerMonitoringExecutionSummary
from .sage_maker_monitoring_schedule_config import SageMakerMonitoringScheduleConfig


class SageMakerDescribeMonitoringScheduleResponse(BaseModel):
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
    ResponseMetadata: dict[str, Any] | None = None
