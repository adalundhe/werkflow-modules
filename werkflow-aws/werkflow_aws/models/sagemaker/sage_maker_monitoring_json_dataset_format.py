from __future__ import annotations
from pydantic import BaseModel, StrictBool


class SageMakerMonitoringJsonDatasetFormat(BaseModel):
    Line: StrictBool | None = None
