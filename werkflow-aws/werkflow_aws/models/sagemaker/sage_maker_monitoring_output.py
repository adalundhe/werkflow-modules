from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_monitoring_s3_output import SageMakerMonitoringS3Output


class SageMakerMonitoringOutput(BaseModel):
    S3Output: SageMakerMonitoringS3Output | None = None
