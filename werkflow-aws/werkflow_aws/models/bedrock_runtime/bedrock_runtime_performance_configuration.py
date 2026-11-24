from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockRuntimePerformanceConfiguration(BaseModel):
    latency: StrictStr | None = None
