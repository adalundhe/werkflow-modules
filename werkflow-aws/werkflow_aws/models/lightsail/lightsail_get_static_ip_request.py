from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailGetStaticIpRequest(BaseModel):
    staticIpName: StrictStr
