from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2TransitGatewayRouteAttachment(BaseModel):
    ResourceId: StrictStr | None = None
    TransitGatewayAttachmentId: StrictStr | None = None
    ResourceType: StrictStr | None = None
