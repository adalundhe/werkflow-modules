from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockAutomatedReasoningPolicyUpdateTypeValue(BaseModel):
    value: StrictStr | None = None
    newValue: StrictStr | None = None
    description: StrictStr | None = None
