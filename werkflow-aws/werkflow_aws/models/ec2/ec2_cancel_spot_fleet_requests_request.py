from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2CancelSpotFleetRequestsRequest(BaseModel):
    SpotFleetRequestIds: list[StrictStr]
    TerminateInstances: StrictBool
    DryRun: StrictBool | None = None
