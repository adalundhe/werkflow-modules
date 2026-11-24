from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2Ipv4PrefixSpecificationRequest(BaseModel):
    Ipv4Prefix: StrictStr | None = None
