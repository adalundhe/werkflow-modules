from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EC2IpamPoolSourceResourceRequest(BaseModel):
    ResourceId: StrictStr | None = None
    ResourceType: Literal['vpc'] | None = None
    ResourceRegion: StrictStr | None = None
    ResourceOwner: StrictStr | None = None
