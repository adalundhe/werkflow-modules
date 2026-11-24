from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTDescribeCustomMetricRequest(BaseModel):
    metricName: StrictStr
