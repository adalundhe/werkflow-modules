from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockAutomatedReasoningPolicyDeleteRuleAnnotation(BaseModel):
    ruleId: StrictStr | None = None
