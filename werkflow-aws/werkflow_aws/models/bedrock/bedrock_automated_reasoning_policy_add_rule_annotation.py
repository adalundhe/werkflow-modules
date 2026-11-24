from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockAutomatedReasoningPolicyAddRuleAnnotation(BaseModel):
    expression: StrictStr | None = None
