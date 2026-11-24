from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDeleteMetricRequest(BaseModel):
    InstanceId: StrictStr
    MetricId: StrictStr
