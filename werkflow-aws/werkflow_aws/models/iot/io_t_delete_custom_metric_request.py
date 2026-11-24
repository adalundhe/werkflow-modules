from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTDeleteCustomMetricRequest(BaseModel):
    metricName: StrictStr
