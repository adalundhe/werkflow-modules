from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class LightsailAttachDiskRequest(BaseModel):
    diskName: StrictStr
    instanceName: StrictStr
    diskPath: StrictStr
    autoMounting: StrictBool | None = None
