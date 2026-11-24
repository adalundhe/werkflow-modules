from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2CancelSpotInstanceRequestsRequest(BaseModel):
    SpotInstanceRequestIds: list[StrictStr]
    DryRun: StrictBool | None = None
