from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DisableVgwRoutePropagationRequest(BaseModel):
    GatewayId: StrictStr
    RouteTableId: StrictStr
    DryRun: StrictBool | None = None
