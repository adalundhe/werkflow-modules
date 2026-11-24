from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ECSMetricConfiguration(BaseModel):
    metricNames: list[StrictStr] | None = None
    resolutionSeconds: StrictInt | None = None
