from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_cancelled_spot_instance_request import EC2CancelledSpotInstanceRequest


class EC2CancelSpotInstanceRequestsResponse(BaseModel):
    CancelledSpotInstanceRequests: list[EC2CancelledSpotInstanceRequest] | None = None
    ResponseMetadata: dict[str, Any] | None = None
