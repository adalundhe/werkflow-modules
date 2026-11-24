from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2CoipCidr(BaseModel):
    Cidr: StrictStr | None = None
    CoipPoolId: StrictStr | None = None
    LocalGatewayRouteTableId: StrictStr | None = None
