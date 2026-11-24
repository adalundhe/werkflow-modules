from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .cloud_watch_dimension_model import CloudWatchDimensionModel


class CloudWatchDescribeAnomalyDetectorsRequest(BaseModel):
    AnomalyDetectorIds: list[StrictStr] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    Namespace: StrictStr | None = None
    MetricName: StrictStr | None = None
    Dimensions: list[CloudWatchDimensionModel] | None = None
    AnomalyDetectorTypes: list[Literal['SINGLE_METRIC', 'METRIC_MATH']] | None = None
