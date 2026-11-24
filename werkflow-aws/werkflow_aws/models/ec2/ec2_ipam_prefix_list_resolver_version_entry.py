from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2IpamPrefixListResolverVersionEntry(BaseModel):
    Cidr: StrictStr | None = None
