from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LightsailAttachedDisk(BaseModel):
    path: StrictStr | None = None
    sizeInGb: StrictInt | None = None
