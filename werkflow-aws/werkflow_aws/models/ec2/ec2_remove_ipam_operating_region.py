from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2RemoveIpamOperatingRegion(BaseModel):
    RegionName: StrictStr | None = None
