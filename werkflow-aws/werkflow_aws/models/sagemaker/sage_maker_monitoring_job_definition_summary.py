from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerMonitoringJobDefinitionSummary(BaseModel):
    MonitoringJobDefinitionName: StrictStr | None = None
    MonitoringJobDefinitionArn: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    EndpointName: StrictStr | None = None
