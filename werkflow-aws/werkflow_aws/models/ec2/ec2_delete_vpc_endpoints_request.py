from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteVpcEndpointsRequest(BaseModel):
    VpcEndpointIds: list[StrictStr]
    DryRun: StrictBool | None = None
