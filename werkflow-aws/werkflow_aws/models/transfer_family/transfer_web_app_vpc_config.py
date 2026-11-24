from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class TransferWebAppVpcConfig(BaseModel):
    SubnetIds: list[StrictStr] | None = None
    VpcId: StrictStr | None = None
    SecurityGroupIds: list[StrictStr] | None = None
    IpAddressType: Literal['IPV4', 'DUALSTACK'] | None = None
