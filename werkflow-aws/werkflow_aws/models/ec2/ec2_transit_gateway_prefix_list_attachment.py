from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2TransitGatewayPrefixListAttachment(BaseModel):
    TransitGatewayAttachmentId: StrictStr | None = None
    ResourceType: StrictStr | None = None
    ResourceId: StrictStr | None = None
