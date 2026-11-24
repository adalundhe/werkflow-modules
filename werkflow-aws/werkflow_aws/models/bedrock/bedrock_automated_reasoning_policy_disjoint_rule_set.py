from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockAutomatedReasoningPolicyDisjointRuleSet(BaseModel):
    variables: list[StrictStr] | None = None
    rules: list[StrictStr] | None = None
