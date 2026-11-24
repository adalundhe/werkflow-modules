from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WAFv2RateLimitJA3Fingerprint(BaseModel):
    FallbackBehavior: StrictStr | None = None
