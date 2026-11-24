from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2AcceptTransitGatewayMulticastDomainAssociationsRequest(BaseModel):
    TransitGatewayMulticastDomainId: StrictStr | None = None
    TransitGatewayAttachmentId: StrictStr | None = None
    SubnetIds: list[StrictStr] | None = None
    DryRun: StrictBool | None = None
