from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt
from .connect_metric_v2 import ConnectMetricV2


class ConnectMetricDataV2(BaseModel):
    Metric: ConnectMetricV2 | None = None
    Value: StrictFloat | StrictInt | None = None
