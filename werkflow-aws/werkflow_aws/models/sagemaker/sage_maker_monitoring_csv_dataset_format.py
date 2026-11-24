from __future__ import annotations
from pydantic import BaseModel, StrictBool


class SageMakerMonitoringCsvDatasetFormat(BaseModel):
    Header: StrictBool | None = None
