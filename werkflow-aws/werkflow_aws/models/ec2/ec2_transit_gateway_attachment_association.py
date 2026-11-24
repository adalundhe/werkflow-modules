from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2TransitGatewayAttachmentAssociation(BaseModel):
    TransitGatewayRouteTableId: StrictStr | None = None
    TransitGatewayPolicyTableId: StrictStr | None = None
    State: StrictStr | None = None
