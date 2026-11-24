from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSGatewayElbNetworkConfiguration(BaseModel):
    inboundSecurityGroup: StrictStr | None = None
    subnets: list[StrictStr] | None = None
    ipAddressType: StrictStr | None = None
