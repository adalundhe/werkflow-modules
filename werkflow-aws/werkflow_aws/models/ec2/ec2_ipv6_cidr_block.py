from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2Ipv6CidrBlock(BaseModel):
    Ipv6CidrBlock: StrictStr | None = None
