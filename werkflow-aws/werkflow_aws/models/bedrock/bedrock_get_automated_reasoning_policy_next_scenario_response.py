from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .bedrock_automated_reasoning_policy_scenario import BedrockAutomatedReasoningPolicyScenario


class BedrockGetAutomatedReasoningPolicyNextScenarioResponse(BaseModel):
    policyArn: StrictStr | None = None
    scenario: BedrockAutomatedReasoningPolicyScenario | None = None
    ResponseMetadata: dict[str, Any] | None = None
