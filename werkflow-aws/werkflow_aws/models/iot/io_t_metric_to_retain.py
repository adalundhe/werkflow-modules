from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .io_t_metric_dimension import IoTMetricDimension


class IoTMetricToRetain(BaseModel):
    metric: StrictStr | None = None
    metricDimension: IoTMetricDimension | None = None
    exportMetric: StrictBool | None = None
