from __future__ import annotations
from pydantic import BaseModel
from .bedrock_automated_reasoning_policy_definition_rule import BedrockAutomatedReasoningPolicyDefinitionRule


class BedrockAutomatedReasoningPolicyUpdateRuleMutation(BaseModel):
    rule: BedrockAutomatedReasoningPolicyDefinitionRule | None = None
