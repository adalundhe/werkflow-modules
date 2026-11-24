from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteTransitGatewayPolicyTableRequest(BaseModel):
    TransitGatewayPolicyTableId: StrictStr
    DryRun: StrictBool | None = None
