from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailAllocateStaticIpRequest(BaseModel):
    staticIpName: StrictStr
