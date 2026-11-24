from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerUpdateMonitoringAlertRequest(BaseModel):
    MonitoringScheduleName: StrictStr
    MonitoringAlertName: StrictStr
    DatapointsToAlert: StrictInt
    EvaluationPeriod: StrictInt
