from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTDescribeFleetMetricRequest(BaseModel):
    metricName: StrictStr
