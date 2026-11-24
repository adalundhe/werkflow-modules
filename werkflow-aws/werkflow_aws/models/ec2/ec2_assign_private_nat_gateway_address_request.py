from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2AssignPrivateNatGatewayAddressRequest(BaseModel):
    NatGatewayId: StrictStr
    PrivateIpAddresses: list[StrictStr] | None = None
    PrivateIpAddressCount: StrictInt | None = None
    DryRun: StrictBool | None = None
