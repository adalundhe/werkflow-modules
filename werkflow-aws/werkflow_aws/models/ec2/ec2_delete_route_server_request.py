from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteRouteServerRequest(BaseModel):
    RouteServerId: StrictStr
    DryRun: StrictBool | None = None
