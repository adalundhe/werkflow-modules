from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class LightsailDeleteDiskRequest(BaseModel):
    diskName: StrictStr
    forceDeleteAddOns: StrictBool | None = None
