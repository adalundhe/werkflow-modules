from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailDetachDiskRequest(BaseModel):
    diskName: StrictStr
