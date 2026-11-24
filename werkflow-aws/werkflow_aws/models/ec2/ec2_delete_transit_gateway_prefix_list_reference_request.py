from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteTransitGatewayPrefixListReferenceRequest(BaseModel):
    TransitGatewayRouteTableId: StrictStr
    PrefixListId: StrictStr
    DryRun: StrictBool | None = None
