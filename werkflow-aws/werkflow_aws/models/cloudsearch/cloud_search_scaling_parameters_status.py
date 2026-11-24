from __future__ import annotations
from pydantic import BaseModel
from .cloud_search_option_status import CloudSearchOptionStatus
from .cloud_search_scaling_parameters import CloudSearchScalingParameters


class CloudSearchScalingParametersStatus(BaseModel):
    Options: CloudSearchScalingParameters | None = None
    Status: CloudSearchOptionStatus | None = None
