from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_spot_fleet_request_config import EC2SpotFleetRequestConfig


class EC2DescribeSpotFleetRequestsResponse(BaseModel):
    NextToken: StrictStr | None = None
    SpotFleetRequestConfigs: list[EC2SpotFleetRequestConfig] | None = None
    ResponseMetadata: dict[str, Any] | None = None
