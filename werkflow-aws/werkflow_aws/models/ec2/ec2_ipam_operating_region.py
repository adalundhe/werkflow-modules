from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2IpamOperatingRegion(BaseModel):
    RegionName: StrictStr | None = None
