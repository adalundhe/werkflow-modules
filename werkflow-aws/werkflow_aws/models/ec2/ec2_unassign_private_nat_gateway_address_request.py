from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2UnassignPrivateNatGatewayAddressRequest(BaseModel):
    NatGatewayId: StrictStr
    PrivateIpAddresses: list[StrictStr]
    MaxDrainDurationSeconds: StrictInt | None = None
    DryRun: StrictBool | None = None
