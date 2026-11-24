from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2TransitGatewayAssociation(BaseModel):
    TransitGatewayRouteTableId: StrictStr | None = None
    TransitGatewayAttachmentId: StrictStr | None = None
    ResourceId: StrictStr | None = None
    ResourceType: StrictStr | None = None
    State: StrictStr | None = None
