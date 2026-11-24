from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailCacheBehaviorPerPath(BaseModel):
    path: StrictStr | None = None
    behavior: StrictStr | None = None
