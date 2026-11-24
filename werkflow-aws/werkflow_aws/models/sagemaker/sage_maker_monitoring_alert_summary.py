from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_monitoring_alert_actions import SageMakerMonitoringAlertActions


class SageMakerMonitoringAlertSummary(BaseModel):
    MonitoringAlertName: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    AlertStatus: StrictStr | None = None
    DatapointsToAlert: StrictInt | None = None
    EvaluationPeriod: StrictInt | None = None
    Actions: SageMakerMonitoringAlertActions | None = None
