from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteRouteServerPeerRequest(BaseModel):
    RouteServerPeerId: StrictStr
    DryRun: StrictBool | None = None
