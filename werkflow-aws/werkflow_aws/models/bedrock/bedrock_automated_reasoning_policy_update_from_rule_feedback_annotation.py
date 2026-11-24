from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockAutomatedReasoningPolicyUpdateFromRuleFeedbackAnnotation(BaseModel):
    ruleIds: list[StrictStr] | None = None
    feedback: StrictStr | None = None
