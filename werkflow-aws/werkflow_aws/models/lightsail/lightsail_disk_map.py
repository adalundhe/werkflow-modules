from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailDiskMap(BaseModel):
    originalDiskPath: StrictStr | None = None
    newDiskName: StrictStr | None = None
