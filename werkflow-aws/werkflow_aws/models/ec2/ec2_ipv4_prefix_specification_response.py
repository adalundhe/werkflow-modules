from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2Ipv4PrefixSpecificationResponse(BaseModel):
    Ipv4Prefix: StrictStr | None = None
