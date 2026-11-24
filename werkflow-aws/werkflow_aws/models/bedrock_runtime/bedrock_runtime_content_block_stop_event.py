from __future__ import annotations
from pydantic import BaseModel, StrictInt


class BedrockRuntimeContentBlockStopEvent(BaseModel):
    contentBlockIndex: StrictInt | None = None
