from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt
from .connect_historical_metric import ConnectHistoricalMetric


class ConnectHistoricalMetricData(BaseModel):
    Metric: ConnectHistoricalMetric | None = None
    Value: StrictFloat | StrictInt | None = None
