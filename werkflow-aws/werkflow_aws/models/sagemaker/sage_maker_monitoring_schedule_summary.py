from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerMonitoringScheduleSummary(BaseModel):
    MonitoringScheduleName: StrictStr | None = None
    MonitoringScheduleArn: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    MonitoringScheduleStatus: StrictStr | None = None
    EndpointName: StrictStr | None = None
    MonitoringJobDefinitionName: StrictStr | None = None
    MonitoringType: StrictStr | None = None
