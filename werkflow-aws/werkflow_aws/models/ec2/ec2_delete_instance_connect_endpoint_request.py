from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteInstanceConnectEndpointRequest(BaseModel):
    InstanceConnectEndpointId: StrictStr
    DryRun: StrictBool | None = None
