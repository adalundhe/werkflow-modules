from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSExpressGatewayServiceNetworkConfiguration(BaseModel):
    securityGroups: list[StrictStr] | None = None
    subnets: list[StrictStr] | None = None
