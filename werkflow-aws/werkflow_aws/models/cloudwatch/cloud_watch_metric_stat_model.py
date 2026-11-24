from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .cloud_watch_metric_model import CloudWatchMetricModel


class CloudWatchMetricStatModel(BaseModel):
    Metric: CloudWatchMetricModel | None = None
    Period: StrictInt | None = None
    Stat: StrictStr | None = None
    Unit: StrictStr | None = None
