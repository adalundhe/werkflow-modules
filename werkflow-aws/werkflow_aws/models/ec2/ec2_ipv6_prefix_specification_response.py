from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2Ipv6PrefixSpecificationResponse(BaseModel):
    Ipv6Prefix: StrictStr | None = None
