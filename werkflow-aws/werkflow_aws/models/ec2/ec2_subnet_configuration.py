from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2SubnetConfiguration(BaseModel):
    SubnetId: StrictStr | None = None
    Ipv4: StrictStr | None = None
    Ipv6: StrictStr | None = None
