from __future__ import annotations
from pydantic import BaseModel
from .bedrock_automated_reasoning_policy_mutation import BedrockAutomatedReasoningPolicyMutation
from .bedrock_automated_reasoning_policy_planning import BedrockAutomatedReasoningPolicyPlanning


class BedrockAutomatedReasoningPolicyBuildStepContext(BaseModel):
    planning: BedrockAutomatedReasoningPolicyPlanning | None = None
    mutation: BedrockAutomatedReasoningPolicyMutation | None = None
