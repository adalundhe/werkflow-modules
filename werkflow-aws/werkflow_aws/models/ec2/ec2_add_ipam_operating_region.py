from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2AddIpamOperatingRegion(BaseModel):
    RegionName: StrictStr | None = None
