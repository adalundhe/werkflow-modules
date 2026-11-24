from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteTransitGatewayRouteRequest(BaseModel):
    TransitGatewayRouteTableId: StrictStr
    DestinationCidrBlock: StrictStr
    DryRun: StrictBool | None = None
