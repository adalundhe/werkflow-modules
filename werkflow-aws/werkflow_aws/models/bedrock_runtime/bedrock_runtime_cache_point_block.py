from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockRuntimeCachePointBlock(BaseModel):
    type: StrictStr | None = None
    ttl: StrictStr | None = None
