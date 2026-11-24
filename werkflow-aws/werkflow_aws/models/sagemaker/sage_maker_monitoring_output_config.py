from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_monitoring_output import SageMakerMonitoringOutput


class SageMakerMonitoringOutputConfig(BaseModel):
    MonitoringOutputs: list[SageMakerMonitoringOutput] | None = None
    KmsKeyId: StrictStr | None = None
