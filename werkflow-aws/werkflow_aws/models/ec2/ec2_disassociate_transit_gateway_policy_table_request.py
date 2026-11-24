from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DisassociateTransitGatewayPolicyTableRequest(BaseModel):
    TransitGatewayPolicyTableId: StrictStr
    TransitGatewayAttachmentId: StrictStr
    DryRun: StrictBool | None = None
