from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_automated_reasoning_policy_definition import BedrockAutomatedReasoningPolicyDefinition


class BedrockUpdateAutomatedReasoningPolicyRequest(BaseModel):
    policyArn: StrictStr
    policyDefinition: BedrockAutomatedReasoningPolicyDefinition
    name: StrictStr | None = None
    description: StrictStr | None = None
