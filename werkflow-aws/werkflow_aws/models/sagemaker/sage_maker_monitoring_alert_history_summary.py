from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerMonitoringAlertHistorySummary(BaseModel):
    MonitoringScheduleName: StrictStr | None = None
    MonitoringAlertName: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    AlertStatus: StrictStr | None = None
