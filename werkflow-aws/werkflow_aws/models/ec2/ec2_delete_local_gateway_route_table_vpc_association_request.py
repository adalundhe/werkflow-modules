from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteLocalGatewayRouteTableVpcAssociationRequest(BaseModel):
    LocalGatewayRouteTableVpcAssociationId: StrictStr
    DryRun: StrictBool | None = None
