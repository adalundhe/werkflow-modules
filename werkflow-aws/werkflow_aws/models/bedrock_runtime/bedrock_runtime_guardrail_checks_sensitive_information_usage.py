from __future__ import annotations
from pydantic import BaseModel, StrictInt


class BedrockRuntimeGuardrailChecksSensitiveInformationUsage(BaseModel):
    textUnits: StrictInt | None = None
