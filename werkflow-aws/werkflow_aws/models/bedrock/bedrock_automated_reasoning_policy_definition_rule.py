from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockAutomatedReasoningPolicyDefinitionRule(BaseModel):
    id: StrictStr | None = None
    expression: StrictStr | None = None
    alternateExpression: StrictStr | None = None
