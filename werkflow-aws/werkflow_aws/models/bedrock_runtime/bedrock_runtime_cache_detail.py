from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BedrockRuntimeCacheDetail(BaseModel):
    ttl: StrictStr | None = None
    inputTokens: StrictInt | None = None
