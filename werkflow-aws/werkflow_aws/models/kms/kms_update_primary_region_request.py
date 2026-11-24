from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KMSUpdatePrimaryRegionRequest(BaseModel):
    KeyId: StrictStr
    PrimaryRegion: StrictStr
