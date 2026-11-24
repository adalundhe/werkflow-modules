from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESPutDedicatedIpInPoolRequest(BaseModel):
    Ip: StrictStr
    DestinationPoolName: StrictStr
