from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailCacheBehavior(BaseModel):
    behavior: StrictStr | None = None
