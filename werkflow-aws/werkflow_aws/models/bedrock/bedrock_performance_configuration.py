from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockPerformanceConfiguration(BaseModel):
    latency: StrictStr | None = None
