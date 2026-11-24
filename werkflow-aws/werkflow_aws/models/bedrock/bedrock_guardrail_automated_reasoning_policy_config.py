from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class BedrockGuardrailAutomatedReasoningPolicyConfig(BaseModel):
    policies: list[StrictStr]
    confidenceThreshold: StrictFloat | StrictInt | None = None
