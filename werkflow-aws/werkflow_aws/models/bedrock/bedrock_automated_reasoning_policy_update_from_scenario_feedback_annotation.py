from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockAutomatedReasoningPolicyUpdateFromScenarioFeedbackAnnotation(BaseModel):
    ruleIds: list[StrictStr] | None = None
    scenarioExpression: StrictStr | None = None
    feedback: StrictStr | None = None
