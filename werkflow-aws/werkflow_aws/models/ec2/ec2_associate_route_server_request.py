from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2AssociateRouteServerRequest(BaseModel):
    RouteServerId: StrictStr
    VpcId: StrictStr
    DryRun: StrictBool | None = None
