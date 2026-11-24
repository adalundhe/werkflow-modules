from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2UpdateVpcLinkRequest(BaseModel):
    VpcLinkId: StrictStr
    Name: StrictStr | None = None
