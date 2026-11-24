from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2GetRouteServerAssociationsRequest(BaseModel):
    RouteServerId: StrictStr
    DryRun: StrictBool | None = None
