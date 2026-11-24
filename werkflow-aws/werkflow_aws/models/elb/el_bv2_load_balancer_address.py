from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ELBv2LoadBalancerAddress(BaseModel):
    IpAddress: StrictStr | None = None
    AllocationId: StrictStr | None = None
    PrivateIPv4Address: StrictStr | None = None
    IPv6Address: StrictStr | None = None
