from __future__ import annotations
from pydantic import BaseModel
from .bedrock_automated_reasoning_policy_definition_rule import BedrockAutomatedReasoningPolicyDefinitionRule


class BedrockAutomatedReasoningPolicyAddRuleMutation(BaseModel):
    rule: BedrockAutomatedReasoningPolicyDefinitionRule | None = None
