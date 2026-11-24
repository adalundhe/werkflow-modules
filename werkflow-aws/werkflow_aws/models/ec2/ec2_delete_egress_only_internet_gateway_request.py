from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteEgressOnlyInternetGatewayRequest(BaseModel):
    EgressOnlyInternetGatewayId: StrictStr
    DryRun: StrictBool | None = None
