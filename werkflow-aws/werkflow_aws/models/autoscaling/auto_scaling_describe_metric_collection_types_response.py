from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .auto_scaling_metric_collection_type import AutoScalingMetricCollectionType
from .auto_scaling_metric_granularity_type import AutoScalingMetricGranularityType


class AutoScalingDescribeMetricCollectionTypesResponse(BaseModel):
    Metrics: list[AutoScalingMetricCollectionType] | None = None
    Granularities: list[AutoScalingMetricGranularityType] | None = None
    ResponseMetadata: dict[str, Any] | None = None
