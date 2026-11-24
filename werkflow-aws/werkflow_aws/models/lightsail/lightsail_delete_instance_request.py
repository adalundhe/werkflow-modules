from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class LightsailDeleteInstanceRequest(BaseModel):
    instanceName: StrictStr
    forceDeleteAddOns: StrictBool | None = None
