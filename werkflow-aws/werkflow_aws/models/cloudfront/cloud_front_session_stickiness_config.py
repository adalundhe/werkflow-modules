from __future__ import annotations
from pydantic import BaseModel, StrictInt


class CloudFrontSessionStickinessConfig(BaseModel):
    IdleTTL: StrictInt | None = None
    MaximumTTL: StrictInt | None = None
