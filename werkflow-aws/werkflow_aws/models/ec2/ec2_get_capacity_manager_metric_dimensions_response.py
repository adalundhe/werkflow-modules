from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_capacity_manager_dimension import EC2CapacityManagerDimension


class EC2GetCapacityManagerMetricDimensionsResponse(BaseModel):
    MetricDimensionResults: list[EC2CapacityManagerDimension] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
