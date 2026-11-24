from __future__ import annotations
from pydantic import BaseModel
from .connect_dimensions import ConnectDimensions
from .connect_historical_metric_data import ConnectHistoricalMetricData


class ConnectHistoricalMetricResult(BaseModel):
    Dimensions: ConnectDimensions | None = None
    Collections: list[ConnectHistoricalMetricData] | None = None
