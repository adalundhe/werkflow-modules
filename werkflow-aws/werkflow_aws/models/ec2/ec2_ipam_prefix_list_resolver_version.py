from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EC2IpamPrefixListResolverVersion(BaseModel):
    Version: StrictInt | None = None
