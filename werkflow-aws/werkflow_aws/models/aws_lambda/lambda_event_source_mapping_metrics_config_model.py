from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaEventSourceMappingMetricsConfigModel(BaseModel):
    Metrics: list[StrictStr] | None = None
