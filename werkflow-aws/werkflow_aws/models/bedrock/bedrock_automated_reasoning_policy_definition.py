from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_automated_reasoning_policy_definition_rule import BedrockAutomatedReasoningPolicyDefinitionRule
from .bedrock_automated_reasoning_policy_definition_type import BedrockAutomatedReasoningPolicyDefinitionType
from .bedrock_automated_reasoning_policy_definition_variable import BedrockAutomatedReasoningPolicyDefinitionVariable


class BedrockAutomatedReasoningPolicyDefinition(BaseModel):
    version: StrictStr | None = None
    types: list[BedrockAutomatedReasoningPolicyDefinitionType] | None = None
    rules: list[BedrockAutomatedReasoningPolicyDefinitionRule] | None = None
    variables: list[BedrockAutomatedReasoningPolicyDefinitionVariable] | None = None
