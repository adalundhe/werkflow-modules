from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_metric_filter_v2 import ConnectMetricFilterV2
from .connect_threshold_v2 import ConnectThresholdV2


class ConnectMetricV2(BaseModel):
    Name: StrictStr | None = None
    Threshold: list[ConnectThresholdV2] | None = None
    MetricId: StrictStr | None = None
    MetricFilters: list[ConnectMetricFilterV2] | None = None
