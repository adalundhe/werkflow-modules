from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EC2DiskImageVolumeDescription(BaseModel):
    Id: StrictStr | None = None
    Size: StrictInt | None = None
