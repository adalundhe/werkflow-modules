from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ModifyInstanceConnectEndpointRequest(BaseModel):
    InstanceConnectEndpointId: StrictStr
    DryRun: StrictBool | None = None
    IpAddressType: Literal['ipv4', 'dualstack', 'ipv6'] | None = None
    SecurityGroupIds: list[StrictStr] | None = None
    PreserveClientIp: StrictBool | None = None
