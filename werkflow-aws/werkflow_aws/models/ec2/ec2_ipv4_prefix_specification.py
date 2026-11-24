from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2Ipv4PrefixSpecification(BaseModel):
    Ipv4Prefix: StrictStr | None = None
