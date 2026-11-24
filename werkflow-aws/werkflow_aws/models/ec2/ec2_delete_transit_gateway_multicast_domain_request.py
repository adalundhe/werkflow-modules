from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteTransitGatewayMulticastDomainRequest(BaseModel):
    TransitGatewayMulticastDomainId: StrictStr
    DryRun: StrictBool | None = None
