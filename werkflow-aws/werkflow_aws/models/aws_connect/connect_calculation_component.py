from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_metric_filter import ConnectMetricFilter


class ConnectCalculationComponent(BaseModel):
    Alias: StrictStr | None = None
    MetricName: StrictStr | None = None
    MetricId: StrictStr | None = None
    MetricFilters: list[ConnectMetricFilter] | None = None
