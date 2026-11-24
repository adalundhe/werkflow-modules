from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt
from .connect_current_metric import ConnectCurrentMetric


class ConnectCurrentMetricData(BaseModel):
    Metric: ConnectCurrentMetric | None = None
    Value: StrictFloat | StrictInt | None = None
