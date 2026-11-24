from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2AssociateTransitGatewayMulticastDomainRequest(BaseModel):
    TransitGatewayMulticastDomainId: StrictStr
    TransitGatewayAttachmentId: StrictStr
    SubnetIds: list[StrictStr]
    DryRun: StrictBool | None = None
