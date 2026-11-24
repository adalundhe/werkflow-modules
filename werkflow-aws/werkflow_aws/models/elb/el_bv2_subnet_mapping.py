from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ELBv2SubnetMapping(BaseModel):
    SubnetId: StrictStr | None = None
    AllocationId: StrictStr | None = None
    PrivateIPv4Address: StrictStr | None = None
    IPv6Address: StrictStr | None = None
    SourceNatIpv6Prefix: StrictStr | None = None
