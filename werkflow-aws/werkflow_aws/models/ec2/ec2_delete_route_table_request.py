from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteRouteTableRequest(BaseModel):
    RouteTableId: StrictStr
    DryRun: StrictBool | None = None
