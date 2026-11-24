from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteTransitGatewayRouteTableRequest(BaseModel):
    TransitGatewayRouteTableId: StrictStr
    DryRun: StrictBool | None = None
