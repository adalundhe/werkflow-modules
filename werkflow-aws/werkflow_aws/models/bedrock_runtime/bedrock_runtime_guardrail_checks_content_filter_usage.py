from __future__ import annotations
from pydantic import BaseModel, StrictInt


class BedrockRuntimeGuardrailChecksContentFilterUsage(BaseModel):
    textUnits: StrictInt | None = None
