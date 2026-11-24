from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteRouteServerEndpointRequest(BaseModel):
    RouteServerEndpointId: StrictStr
    DryRun: StrictBool | None = None
