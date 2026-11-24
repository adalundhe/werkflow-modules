from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2AssociateTransitGatewayPolicyTableRequest(BaseModel):
    TransitGatewayPolicyTableId: StrictStr
    TransitGatewayAttachmentId: StrictStr
    DryRun: StrictBool | None = None
