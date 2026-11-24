from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudFrontOriginShield(BaseModel):
    Enabled: StrictBool | None = None
    OriginShieldRegion: StrictStr | None = None
