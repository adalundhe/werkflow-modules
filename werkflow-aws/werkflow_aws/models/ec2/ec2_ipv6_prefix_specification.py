from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2Ipv6PrefixSpecification(BaseModel):
    Ipv6Prefix: StrictStr | None = None
