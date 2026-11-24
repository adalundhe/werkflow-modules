from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayDeleteVpcLinkRequest(BaseModel):
    vpcLinkId: StrictStr
