from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDescribeMetricRequest(BaseModel):
    InstanceId: StrictStr
    MetricId: StrictStr
