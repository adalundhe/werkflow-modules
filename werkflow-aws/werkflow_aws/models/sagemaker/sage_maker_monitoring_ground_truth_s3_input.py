from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerMonitoringGroundTruthS3Input(BaseModel):
    S3Uri: StrictStr | None = None
