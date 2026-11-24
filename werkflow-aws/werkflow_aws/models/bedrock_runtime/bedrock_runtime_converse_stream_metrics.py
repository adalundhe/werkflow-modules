from __future__ import annotations
from pydantic import BaseModel, StrictInt


class BedrockRuntimeConverseStreamMetrics(BaseModel):
    latencyMs: StrictInt | None = None
