from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IoTDeleteFleetMetricRequest(BaseModel):
    metricName: StrictStr
    expectedVersion: StrictInt | None = None
