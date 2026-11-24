from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerMonitoringConstraintsResource(BaseModel):
    S3Uri: StrictStr | None = None
