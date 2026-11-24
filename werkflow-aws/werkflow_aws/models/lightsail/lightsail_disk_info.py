from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class LightsailDiskInfo(BaseModel):
    name: StrictStr | None = None
    path: StrictStr | None = None
    sizeInGb: StrictInt | None = None
    isSystemDisk: StrictBool | None = None
