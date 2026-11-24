from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTUpdateCustomMetricRequest(BaseModel):
    metricName: StrictStr
    displayName: StrictStr
