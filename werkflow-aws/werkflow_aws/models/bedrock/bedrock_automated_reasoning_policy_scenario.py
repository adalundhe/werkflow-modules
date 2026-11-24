from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockAutomatedReasoningPolicyScenario(BaseModel):
    expression: StrictStr | None = None
    alternateExpression: StrictStr | None = None
    expectedResult: StrictStr | None = None
    ruleIds: list[StrictStr] | None = None
