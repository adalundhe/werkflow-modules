from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockAutomatedReasoningPolicyDefinitionTypeValue(BaseModel):
    value: StrictStr | None = None
    description: StrictStr | None = None
