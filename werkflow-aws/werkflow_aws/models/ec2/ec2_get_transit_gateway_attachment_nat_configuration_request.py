from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2GetTransitGatewayAttachmentNatConfigurationRequest(BaseModel):
    TransitGatewayAttachmentId: StrictStr
    DryRun: StrictBool | None = None
