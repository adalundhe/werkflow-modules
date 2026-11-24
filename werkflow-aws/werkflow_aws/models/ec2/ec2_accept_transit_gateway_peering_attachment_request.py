from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2AcceptTransitGatewayPeeringAttachmentRequest(BaseModel):
    TransitGatewayAttachmentId: StrictStr
    DryRun: StrictBool | None = None
