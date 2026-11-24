from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2InstanceIpv6Address(BaseModel):
    Ipv6Address: StrictStr | None = None
    IsPrimaryIpv6: StrictBool | None = None
