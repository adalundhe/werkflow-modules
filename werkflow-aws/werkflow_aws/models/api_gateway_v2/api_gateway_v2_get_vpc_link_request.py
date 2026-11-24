from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2GetVpcLinkRequest(BaseModel):
    VpcLinkId: StrictStr
