from __future__ import annotations
from pydantic import BaseModel
from .connect_current_metric_data import ConnectCurrentMetricData
from .connect_dimensions import ConnectDimensions


class ConnectCurrentMetricResult(BaseModel):
    Dimensions: ConnectDimensions | None = None
    Collections: list[ConnectCurrentMetricData] | None = None
