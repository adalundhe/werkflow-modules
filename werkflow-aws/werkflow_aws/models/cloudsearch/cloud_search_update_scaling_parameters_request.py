from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_search_scaling_parameters import CloudSearchScalingParameters


class CloudSearchUpdateScalingParametersRequest(BaseModel):
    DomainName: StrictStr
    ScalingParameters: CloudSearchScalingParameters
