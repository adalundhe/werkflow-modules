from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2TransitGatewayRouteTablePropagation(BaseModel):
    TransitGatewayAttachmentId: StrictStr | None = None
    ResourceId: StrictStr | None = None
    ResourceType: StrictStr | None = None
    State: StrictStr | None = None
    TransitGatewayRouteTableAnnouncementId: StrictStr | None = None
