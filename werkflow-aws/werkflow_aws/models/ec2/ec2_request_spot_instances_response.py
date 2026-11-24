from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_spot_instance_request import EC2SpotInstanceRequest


class EC2RequestSpotInstancesResponse(BaseModel):
    SpotInstanceRequests: list[EC2SpotInstanceRequest] | None = None
    ResponseMetadata: dict[str, Any] | None = None
