from __future__ import annotations
from pydantic import BaseModel, StrictInt


class BedrockRuntimeGuardrailImageCoverage(BaseModel):
    guarded: StrictInt | None = None
    total: StrictInt | None = None
