from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2SubnetIpPrefixes(BaseModel):
    SubnetId: StrictStr | None = None
    IpPrefixes: list[StrictStr] | None = None
