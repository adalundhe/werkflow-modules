from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2InstanceIpv6AddressRequest(BaseModel):
    Ipv6Address: StrictStr | None = None
