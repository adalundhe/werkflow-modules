from __future__ import annotations
from pydantic import BaseModel
from .emrs3_monitoring_configuration import EMRS3MonitoringConfiguration


class EMRStepMonitoringConfiguration(BaseModel):
    S3MonitoringConfiguration: EMRS3MonitoringConfiguration | None = None
