from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .io_t_behavior_criteria import IoTBehaviorCriteria
from .io_t_metric_dimension import IoTMetricDimension


class IoTBehavior(BaseModel):
    name: StrictStr | None = None
    metric: StrictStr | None = None
    metricDimension: IoTMetricDimension | None = None
    criteria: IoTBehaviorCriteria | None = None
    suppressAlerts: StrictBool | None = None
    exportMetric: StrictBool | None = None
