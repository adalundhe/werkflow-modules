from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_cancel_spot_fleet_requests_error_item import EC2CancelSpotFleetRequestsErrorItem
from .ec2_cancel_spot_fleet_requests_success_item import EC2CancelSpotFleetRequestsSuccessItem


class EC2CancelSpotFleetRequestsResponse(BaseModel):
    SuccessfulFleetRequests: list[EC2CancelSpotFleetRequestsSuccessItem] | None = None
    UnsuccessfulFleetRequests: list[EC2CancelSpotFleetRequestsErrorItem] | None = None
    ResponseMetadata: dict[str, Any] | None = None
