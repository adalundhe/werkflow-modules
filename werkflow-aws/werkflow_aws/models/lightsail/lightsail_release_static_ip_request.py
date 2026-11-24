from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailReleaseStaticIpRequest(BaseModel):
    staticIpName: StrictStr
