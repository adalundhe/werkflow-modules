from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailStopInstanceOnIdleRequest(BaseModel):
    threshold: StrictStr | None = None
    duration: StrictStr | None = None
