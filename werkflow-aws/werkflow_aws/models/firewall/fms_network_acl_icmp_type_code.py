from __future__ import annotations
from pydantic import BaseModel, StrictInt


class FMSNetworkAclIcmpTypeCode(BaseModel):
    Code: StrictInt | None = None
    Type: StrictInt | None = None
