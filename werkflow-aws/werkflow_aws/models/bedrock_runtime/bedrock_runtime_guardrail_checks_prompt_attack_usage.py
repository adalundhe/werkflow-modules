from __future__ import annotations
from pydantic import BaseModel, StrictInt


class BedrockRuntimeGuardrailChecksPromptAttackUsage(BaseModel):
    textUnits: StrictInt | None = None
