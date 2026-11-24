from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockRuntimeGuardrailAutomatedReasoningRule(BaseModel):
    identifier: StrictStr | None = None
    policyVersionArn: StrictStr | None = None
