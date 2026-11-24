from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_watch_dimension_model import CloudWatchDimensionModel


class CloudWatchSingleMetricAnomalyDetector(BaseModel):
    AccountId: StrictStr | None = None
    Namespace: StrictStr | None = None
    MetricName: StrictStr | None = None
    Dimensions: list[CloudWatchDimensionModel] | None = None
    Stat: StrictStr | None = None
