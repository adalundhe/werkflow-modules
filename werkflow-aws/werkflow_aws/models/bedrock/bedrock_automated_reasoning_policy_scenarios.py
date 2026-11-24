from __future__ import annotations
from pydantic import BaseModel
from .bedrock_automated_reasoning_policy_scenario import BedrockAutomatedReasoningPolicyScenario


class BedrockAutomatedReasoningPolicyScenarios(BaseModel):
    policyScenarios: list[BedrockAutomatedReasoningPolicyScenario] | None = None
