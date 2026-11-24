from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerMonitoringExecutionSummary(BaseModel):
    MonitoringScheduleName: StrictStr | None = None
    ScheduledTime: datetime.datetime | StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    MonitoringExecutionStatus: StrictStr | None = None
    ProcessingJobArn: StrictStr | None = None
    EndpointName: StrictStr | None = None
    FailureReason: StrictStr | None = None
    MonitoringJobDefinitionName: StrictStr | None = None
    MonitoringType: StrictStr | None = None
