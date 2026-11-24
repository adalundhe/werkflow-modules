from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayGetVpcLinkRequest(BaseModel):
    vpcLinkId: StrictStr
