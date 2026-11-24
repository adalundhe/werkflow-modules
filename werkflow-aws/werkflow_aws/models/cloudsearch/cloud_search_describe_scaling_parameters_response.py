from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_search_scaling_parameters_status import CloudSearchScalingParametersStatus


class CloudSearchDescribeScalingParametersResponse(BaseModel):
    ScalingParameters: CloudSearchScalingParametersStatus | None = None
    ResponseMetadata: dict[str, Any] | None = None
