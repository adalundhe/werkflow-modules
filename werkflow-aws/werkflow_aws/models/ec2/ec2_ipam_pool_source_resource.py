from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2IpamPoolSourceResource(BaseModel):
    ResourceId: StrictStr | None = None
    ResourceType: StrictStr | None = None
    ResourceRegion: StrictStr | None = None
    ResourceOwner: StrictStr | None = None
