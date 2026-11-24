from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SESPutDedicatedIpWarmupAttributesRequest(BaseModel):
    Ip: StrictStr
    WarmupPercentage: StrictInt
