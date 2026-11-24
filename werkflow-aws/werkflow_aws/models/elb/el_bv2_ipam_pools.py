from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ELBv2IpamPools(BaseModel):
    Ipv4IpamPoolId: StrictStr | None = None
