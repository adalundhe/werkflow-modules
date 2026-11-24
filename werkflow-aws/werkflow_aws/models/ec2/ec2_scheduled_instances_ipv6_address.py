from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2ScheduledInstancesIpv6Address(BaseModel):
    Ipv6Address: StrictStr | None = None
