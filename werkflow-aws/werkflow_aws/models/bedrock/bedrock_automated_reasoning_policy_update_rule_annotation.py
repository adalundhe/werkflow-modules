from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockAutomatedReasoningPolicyUpdateRuleAnnotation(BaseModel):
    ruleId: StrictStr | None = None
    expression: StrictStr | None = None
