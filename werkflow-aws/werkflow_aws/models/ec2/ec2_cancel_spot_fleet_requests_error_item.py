from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_cancel_spot_fleet_requests_error import EC2CancelSpotFleetRequestsError


class EC2CancelSpotFleetRequestsErrorItem(BaseModel):
    Error: EC2CancelSpotFleetRequestsError | None = None
    SpotFleetRequestId: StrictStr | None = None
