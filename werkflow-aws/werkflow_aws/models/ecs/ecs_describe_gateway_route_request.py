from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSDescribeGatewayRouteRequest(BaseModel):
    gatewayRouteArn: StrictStr
