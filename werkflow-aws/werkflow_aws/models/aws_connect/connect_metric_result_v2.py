from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_metric_data_v2 import ConnectMetricDataV2
from .connect_metric_interval import ConnectMetricInterval


class ConnectMetricResultV2(BaseModel):
    Dimensions: dict[StrictStr, StrictStr] | None = None
    MetricInterval: ConnectMetricInterval | None = None
    Collections: list[ConnectMetricDataV2] | None = None
