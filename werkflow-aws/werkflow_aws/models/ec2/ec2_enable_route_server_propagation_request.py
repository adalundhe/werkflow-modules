from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2EnableRouteServerPropagationRequest(BaseModel):
    RouteServerId: StrictStr
    RouteTableId: StrictStr
    DryRun: StrictBool | None = None
