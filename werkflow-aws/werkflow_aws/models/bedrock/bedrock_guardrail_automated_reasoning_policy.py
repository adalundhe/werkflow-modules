from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class BedrockGuardrailAutomatedReasoningPolicy(BaseModel):
    policies: list[StrictStr] | None = None
    confidenceThreshold: StrictFloat | StrictInt | None = None
