from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailAttachStaticIpRequest(BaseModel):
    staticIpName: StrictStr
    instanceName: StrictStr
