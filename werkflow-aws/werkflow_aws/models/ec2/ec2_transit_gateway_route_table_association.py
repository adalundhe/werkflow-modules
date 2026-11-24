from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2TransitGatewayRouteTableAssociation(BaseModel):
    TransitGatewayAttachmentId: StrictStr | None = None
    ResourceId: StrictStr | None = None
    ResourceType: StrictStr | None = None
    State: StrictStr | None = None
