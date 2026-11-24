from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteLocalGatewayRouteTableRequest(BaseModel):
    LocalGatewayRouteTableId: StrictStr
    DryRun: StrictBool | None = None
