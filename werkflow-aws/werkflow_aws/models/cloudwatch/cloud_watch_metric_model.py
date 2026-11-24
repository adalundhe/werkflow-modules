from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_watch_dimension_model import CloudWatchDimensionModel


class CloudWatchMetricModel(BaseModel):
    Namespace: StrictStr | None = None
    MetricName: StrictStr | None = None
    Dimensions: list[CloudWatchDimensionModel] | None = None
