from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2GetRouteServerPropagationsRequest(BaseModel):
    RouteServerId: StrictStr
    RouteTableId: StrictStr | None = None
    DryRun: StrictBool | None = None
