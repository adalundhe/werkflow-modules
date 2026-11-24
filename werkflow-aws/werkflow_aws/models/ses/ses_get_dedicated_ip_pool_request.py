from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESGetDedicatedIpPoolRequest(BaseModel):
    PoolName: StrictStr
