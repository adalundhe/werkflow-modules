from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2AttachInternetGatewayRequest(BaseModel):
    InternetGatewayId: StrictStr
    VpcId: StrictStr
    DryRun: StrictBool | None = None
