from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EFSCreateMountTargetRequest(BaseModel):
    FileSystemId: StrictStr
    SubnetId: StrictStr
    IpAddress: StrictStr | None = None
    Ipv6Address: StrictStr | None = None
    IpAddressType: Literal['IPV4_ONLY', 'IPV6_ONLY', 'DUAL_STACK'] | None = None
    SecurityGroups: list[StrictStr] | None = None
