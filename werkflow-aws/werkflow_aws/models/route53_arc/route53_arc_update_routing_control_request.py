from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53ARCUpdateRoutingControlRequest(BaseModel):
    RoutingControlArn: StrictStr
    RoutingControlName: StrictStr
