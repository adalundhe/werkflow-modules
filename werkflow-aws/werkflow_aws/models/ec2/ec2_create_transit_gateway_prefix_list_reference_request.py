from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2CreateTransitGatewayPrefixListReferenceRequest(BaseModel):
    TransitGatewayRouteTableId: StrictStr
    PrefixListId: StrictStr
    TransitGatewayAttachmentId: StrictStr | None = None
    Blackhole: StrictBool | None = None
    DryRun: StrictBool | None = None
