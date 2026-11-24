from __future__ import annotations
from pydantic import BaseModel, StrictInt


class BedrockRuntimeConverseMetrics(BaseModel):
    latencyMs: StrictInt | None = None
