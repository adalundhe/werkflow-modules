from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DisableRouteServerPropagationRequest(BaseModel):
    RouteServerId: StrictStr
    RouteTableId: StrictStr
    DryRun: StrictBool | None = None
