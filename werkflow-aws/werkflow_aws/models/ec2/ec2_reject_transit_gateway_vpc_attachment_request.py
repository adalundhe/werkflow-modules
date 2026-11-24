from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2RejectTransitGatewayVpcAttachmentRequest(BaseModel):
    TransitGatewayAttachmentId: StrictStr
    DryRun: StrictBool | None = None
